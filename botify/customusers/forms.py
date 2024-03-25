from django.forms import ModelForm
from customusers.models import User
from django import forms


class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'class': 'input', 'placeholder': 'Password'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'placeholder': 'Email'}
            )
        }