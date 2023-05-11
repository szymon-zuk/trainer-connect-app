from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .models import Exercise


class MainPage(View):
    def get(self, request):
        return render(request, "base.html")


class AddExerciseView(CreateView):
    model = Exercise
    success_url = reverse_lazy('main-page')
    fields = '__all__'
    success_message = 'Dodano ćwiczenie!'

    def get_success_message(self, cleaned_data):
        return f"Dodano ćwiczenie {cleaned_data['name']}"