from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Habit

class DashboardContextMixin:
    """Mixin para agregar contexto común del dashboard a las vistas"""
    
    def get_dashboard_context(self, **kwargs):
        """Obtiene el contexto común para el dashboard"""
        context = {
            'page_title': getattr(self, 'page_title', 'Dashboard'),
            'action_button_url': getattr(self, 'action_button_url', None),
            'action_button_text': getattr(self, 'action_button_text', None),
        }
        context.update(kwargs)
        return context

class HabitOwnerMixin(LoginRequiredMixin):
    """Mixin para verificar que el usuario es dueño del hábito"""
    
    def get_habit(self, habit_id):
        """Obtiene un hábito verificando que pertenece al usuario"""
        return get_object_or_404(Habit, id=habit_id, user=self.request.user) 