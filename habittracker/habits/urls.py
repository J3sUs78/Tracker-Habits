from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/', views.edit_profile, name='edit_profile'),
    path('crear-habito/', views.create_habit, name='create_habit'),
    path('editar-habito/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('eliminar-habito/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('toggle-habito/<int:habit_id>/', views.toggle_habit_status, name='toggle_habit_status'),
] 