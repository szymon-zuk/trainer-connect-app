from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from .models import Exercise, Training, TrainingPlan
from .forms import ExerciseForm, TrainingForm, TrainingPlanForm


class MainPage(View):
    """View of the default page"""

    def get(self, request):
        return render(request, "main_page.html")


class AddExerciseView(CreateView):
    """Implements a form that adds an exercise to database"""

    model = Exercise
    success_url = reverse_lazy("main-page")
    form_class = ExerciseForm
    success_message = "Dodano ćwiczenie!"

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
    success_message = "Dodano trening!"

    def get_success_message(self, cleaned_data):
        return f"Dodano trening {cleaned_data['name']}"


class TrainingListView(ListView):
    model = Training
    paginate_by = 30


class AddTrainingPlanView(CreateView):
    model = TrainingPlan
    success_url = reverse_lazy("main-page")
    form_class = TrainingPlanForm
    success_message = "Dodano plan treningowy!"

    def get_success_message(self, cleaned_data):
        return f"Dodano plan treningowy {cleaned_data['name']}"


class TrainingPlanListView(ListView):
    model = TrainingPlan
    paginate_by = 30
    context_object_name = 'training_plan_list'
    template_name = "trainingplan_list.html"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return TrainingPlan.objects.filter(name__icontains=query)
        else:
            return TrainingPlan.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class TraineeListView(View):
    def get(self, request):
        trainees = User.objects.all()
        ctx = {
            'trainees': trainees,
        }
        return render(request, "trainee_list.html", ctx)
