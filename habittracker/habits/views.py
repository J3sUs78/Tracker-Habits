from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'habits/index.html')

def login_view(request):
    return render(request, 'habits/login.html')

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
