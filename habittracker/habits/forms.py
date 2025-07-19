from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, Habit, Category

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'required': True}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email ya está registrado.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        # Validación de que ambas contraseñas estén presentes
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('Las contraseñas no coinciden. Por favor, asegúrate de escribir la misma contraseña en ambos campos.')
            
            # Validación de seguridad de contraseña
            try:
                validate_password(password1)
            except ValidationError as e:
                self.add_error('password1', e)
        elif password1 and not password2:
            raise ValidationError('Por favor, confirma tu contraseña.')
        elif password2 and not password1:
            raise ValidationError('Por favor, ingresa tu contraseña.')
        
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'notification_enabled']
        labels = {
            'phone': 'Teléfono',
            'notification_enabled': '¿Recibir notificaciones?'
        }

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['nombre', 'descripcion', 'periodicidad', 'meta', 'categoria', 'activo']
        labels = {
            'nombre': 'Nombre del hábito',
            'descripcion': 'Descripción (opcional)',
            'periodicidad': '¿Con qué frecuencia?',
            'meta': 'Meta (veces por periodo)',
            'categoria': 'Categoría',
            'activo': '¿Activo?'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Hacer ejercicio, Leer 30 minutos, Meditar...',
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Describe tu hábito (opcional)',
                'rows': 3,
                'class': 'form-control'
            }),
            'periodicidad': forms.Select(attrs={'class': 'form-control'}),
            'meta': forms.NumberInput(attrs={
                'min': 1,
                'max': 100,
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError('Usuario o contraseña incorrectos.')
        return cleaned_data 