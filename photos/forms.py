from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': "Nom d'utilisateur"
                                               }),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                   'type': 'password',
                                                   'placeholder': 'Mot de passe'})
        }

