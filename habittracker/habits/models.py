from django.db import models
from django.contrib.auth.models import User
from .constants import PERIODICIDAD_CHOICES

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    notification_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    periodicidad = models.CharField(max_length=10, choices=PERIODICIDAD_CHOICES, default='diario')
    meta = models.IntegerField(default=1, help_text='¿Cuántas veces cumplirlo en el periodo?')
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='habits')

    def __str__(self):
        return f"{self.nombre} ({self.user.username})"

class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.nombre} - {self.fecha} - {'Completado' if self.completado else 'Pendiente'}"
