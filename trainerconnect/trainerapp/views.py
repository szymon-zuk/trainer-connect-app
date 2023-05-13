from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from .models import Exercise, Training
from .forms import ExerciseForm, TrainingForm


class MainPage(View):
    """ View of the default page"""
    def get(self, request):
        return render(request, "base.html")


class AddExerciseView(CreateView):
    """Implements a form that adds an exercise to database"""
    model = Exercise
    success_url = reverse_lazy('main-page')
    form_class = ExerciseForm
    success_message = 'Dodano ćwiczenie!'

    def get_success_message(self, cleaned_data):
        return f"Dodano ćwiczenie {cleaned_data['name']}"


class ExerciseListView(ListView):
    """Shows a list of all exercises"""
    model = Exercise
    paginate_by = 30


class AddTrainingView(CreateView):
    """Implements a form that adds a training to database"""
    model = Training
    success_url = reverse_lazy("main-page")
    form_class = TrainingForm
    success_message = 'Dodano trening!'

    def get_success_message(self, cleaned_data):
        return f"Dodano trening {cleaned_data['name']}"