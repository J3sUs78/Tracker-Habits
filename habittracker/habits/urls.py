from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('perfil/', views.edit_profile, name='edit_profile'),
    path('crear-habito/', views.create_habit, name='create_habit'),
] 