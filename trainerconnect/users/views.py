from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegisterForm


class AppLoginView(LoginView):
    template_name = "registrations/login.html"

    def get_success_url(self) -> str:
        return reverse_lazy("main-page")

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "Niepoprawny login lub hasło!")
        return self.render_to_response(self.get_context_data(form=form))


class AppLogoutView(LogoutView):
    template_name = "registrations/logged_out.html"

    def get_success_url(self):
        return reverse_lazy("main-page")


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registrations/register.html"
