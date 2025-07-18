from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email ya está registrado.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return cleaned_data 