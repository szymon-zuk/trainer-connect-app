from django.db import models
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages


class AppLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/registration/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy("main-page")
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Niepoprawny login lub hasło!')
        return self.render_to_response(self.get_context_data(form=form))
    

