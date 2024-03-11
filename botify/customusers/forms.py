from django.forms import ModelForm
from customusers.models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']