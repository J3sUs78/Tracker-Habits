from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm, LoginForm, UserProfileForm, HabitForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Habit, HabitRecord
from django.http import JsonResponse
from django.db.models import Count, Q
from datetime import datetime, timedelta

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'habits/index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'habits/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            messages.success(request, 'Usuario registrado correctamente. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'habits/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('index')

@login_required
def dashboard(request):
    habits = Habit.objects.filter(user=request.user).order_by('-fecha_creacion')
    
    # Estadísticas
    total_habits = habits.count()
    active_habits = habits.filter(activo=True).count()
    inactive_habits = habits.filter(activo=False).count()
    
    # Hábitos por categoría
    habits_by_category = habits.values('categoria__name').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Hábitos por periodicidad
    habits_by_periodicity = habits.values('periodicidad').annotate(
        count=Count('id')
    ).order_by('-count')
    
    context = {
        'habits': habits,
        'total_habits': total_habits,
        'active_habits': active_habits,
        'inactive_habits': inactive_habits,
        'habits_by_category': habits_by_category,
        'habits_by_periodicity': habits_by_periodicity,
    }
    
    return render(request, 'habits/dashboard.html', context)

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('edit_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'habits/edit_profile.html', {'form': form})

@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, 'Hábito creado correctamente.')
            return redirect('dashboard')
    else:
        form = HabitForm()
    return render(request, 'habits/create_habit.html', {'form': form})

@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hábito actualizado correctamente.')
            return redirect('dashboard')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/edit_habit.html', {'form': form, 'habit': habit})

@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        messages.success(request, 'Hábito eliminado correctamente.')
        return redirect('dashboard')
    return render(request, 'habits/delete_habit.html', {'habit': habit})

@login_required
def toggle_habit_status(request, habit_id):
    if request.method == 'POST':
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        habit.activo = not habit.activo
        habit.save()
        return JsonResponse({'status': 'success', 'activo': habit.activo})
    return JsonResponse({'status': 'error'}, status=400)
