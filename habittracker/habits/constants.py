# Constantes para el proyecto Habit Tracker

# Periodicidades disponibles
PERIODICIDAD_CHOICES = [
    ('diario', 'Diario'),
    ('semanal', 'Semanal'),
    ('mensual', 'Mensual'),
]

# Categorías predefinidas con emojis
DEFAULT_CATEGORIES = [
    {
        'name': '🏥 Salud y Bienestar',
        'description': 'Hábitos relacionados con la salud física y mental'
    },
    {
        'name': '⚡ Productividad',
        'description': 'Hábitos para mejorar la eficiencia y organización'
    },
    {
        'name': '📚 Aprendizaje',
        'description': 'Hábitos para el desarrollo personal y profesional'
    },
    {
        'name': '💰 Finanzas',
        'description': 'Hábitos para el manejo del dinero y ahorro'
    },
    {
        'name': '❤️ Relaciones',
        'description': 'Hábitos para mejorar las relaciones personales'
    },
    {
        'name': '💪 Ejercicio',
        'description': 'Hábitos de actividad física y deporte'
    },
    {
        'name': '🥗 Alimentación',
        'description': 'Hábitos de nutrición y alimentación saludable'
    },
    {
        'name': '🧘 Meditación',
        'description': 'Hábitos de mindfulness y relajación'
    },
    {
        'name': '🧹 Limpieza',
        'description': 'Hábitos de organización y limpieza personal'
    },
    {
        'name': '🎨 Creatividad',
        'description': 'Hábitos para desarrollar la creatividad y hobbies'
    }
]

# Mensajes de éxito
SUCCESS_MESSAGES = {
    'habit_created': 'Hábito creado correctamente.',
    'habit_updated': 'Hábito actualizado correctamente.',
    'habit_deleted': 'Hábito eliminado correctamente.',
    'profile_updated': 'Perfil actualizado correctamente.',
    'user_registered': 'Usuario registrado correctamente. Ahora puedes iniciar sesión.',
    'logout_success': 'Has cerrado sesión correctamente.',
}

# Mensajes de error
ERROR_MESSAGES = {
    'login_failed': 'Usuario o contraseña incorrectos.',
    'email_exists': 'Este email ya está registrado.',
    'passwords_dont_match': 'Las contraseñas no coinciden.',
    'confirm_password_required': 'Por favor, confirma tu contraseña.',
    'password_required': 'Por favor, ingresa tu contraseña.',
} 