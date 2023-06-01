from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Form to register a new user"""

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "username": "Login",
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "email": "e-mail",
            "password1": "Hasło",
            "password2": "Powtórz hasło",
        }
