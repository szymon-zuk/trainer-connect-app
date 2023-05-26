from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Opcjonalne")
    last_name = forms.CharField(max_length=30, required=False, help_text="Opcjonalne")
    email = forms.EmailField(max_length=254, help_text="Wpisz swój adres e-mail")

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
