from django.db.models import Count
from .models import Habit

def get_user_stats(user):
    """Obtiene estadísticas del usuario"""
    habits = Habit.objects.filter(user=user)
    
    return {
        'total_habits': habits.count(),
        'active_habits': habits.filter(activo=True).count(),
        'inactive_habits': habits.filter(activo=False).count(),
        'habits_by_category': habits.values('categoria__name').annotate(
            count=Count('id')
        ).order_by('-count'),
        'habits_by_periodicity': habits.values('periodicidad').annotate(
            count=Count('id')
        ).order_by('-count'),
    }

def get_dashboard_context(user, **extra_context):
    """Obtiene el contexto completo para el dashboard"""
    stats = get_user_stats(user)
    habits = Habit.objects.filter(user=user).order_by('-fecha_creacion')
    
    context = {
        'habits': habits,
        'page_title': 'Mi Dashboard',
        'action_button_url': 'create_habit',
        'action_button_text': '➕ Nuevo Hábito',
        **stats,
        **extra_context
    }
    
    return context 