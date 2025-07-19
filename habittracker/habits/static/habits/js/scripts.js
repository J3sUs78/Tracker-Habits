document.addEventListener('DOMContentLoaded', function() {
    // Toggle habit status
    const toggleButtons = document.querySelectorAll('.btn-toggle');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const habitId = this.getAttribute('data-habit-id');
            const isActive = this.getAttribute('data-active') === 'true';
            
            fetch(`/toggle-habito/${habitId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Update button appearance
                    this.setAttribute('data-active', data.activo);
                    this.textContent = data.activo ? '🟢' : '🔴';
                    
                    // Update card appearance
                    const card = this.closest('.habit-card');
                    if (data.activo) {
                        card.classList.remove('inactive');
                    } else {
                        card.classList.add('inactive');
                    }
                    
                    // Update status badge
                    const statusBadge = card.querySelector('.status-badge');
                    if (statusBadge) {
                        statusBadge.textContent = data.activo ? 'Activo' : 'Inactivo';
                        statusBadge.className = `status-badge ${data.activo ? 'active' : 'inactive'}`;
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al cambiar el estado del hábito');
            });
        });
    });
    
    // Confirm delete
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que quieres eliminar este hábito?')) {
                e.preventDefault();
            }
        });
    });
});

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
