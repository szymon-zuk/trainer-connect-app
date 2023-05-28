from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Exercise, Training, TrainingPlan
from .forms import ExerciseForm, TrainingForm, TrainingPlanForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPage(View):
    """View of the default page"""

    def get(self, request):
        return render(request, "main_page.html")


class AddExerciseView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Implements a form that adds an exercise to database"""

    model = Exercise
    success_url = reverse_lazy("exercise-list")
    form_class = ExerciseForm
    template_name = "trainerapp/exercise_form.html"
    success_message = "Dodano ćwiczenie!"


class ExerciseListView(LoginRequiredMixin, ListView):
    """Shows a list of all exercises"""

    model = Exercise
    redirect_field_name = reverse_lazy("exercise-list")

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return Exercise.objects.filter(name__icontains=query)
        else:
            return Exercise.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        return context


class UpdateExerciseView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """A view that lets you update the properties of an exercise"""

    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy("exercise-list")
    template_name_suffix = "_update_form"
    success_message = "Zaktualizowano ćwiczenie!"


class DeleteExerciseView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """A view that lets you delete a single exercise"""

    model = Exercise
    success_url = reverse_lazy("exercise-list")
    success_message = "Usunięto ćwiczenie!"
    redirect_field_name = reverse_lazy("delete-exercise")


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    """Detailed information about exercise"""

    model = Exercise
    redirect_field_name = reverse_lazy("exercise-update")


class AddTrainingView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Implements a form that adds a training to database"""

    model = Training
    success_url = reverse_lazy("training-list")
    form_class = TrainingForm
    redirect_field_name = reverse_lazy("add-training")
    success_message = "Dodano trening!"


class TrainingListView(LoginRequiredMixin, ListView):
    """List view of all trainings"""

    model = Training
    redirect_field_name = reverse_lazy("training-list")

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return Training.objects.filter(name__icontains=query)
        else:
            return Training.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        return context


class UpdateTrainingView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view of a single training"""

    model = Training
    template_name_suffix = "_update_form"
    form_class = TrainingForm
    success_url = reverse_lazy("training-list")
    success_message = "Zaktualizowano trening!"


class TrainingDetailView(LoginRequiredMixin, DetailView):
    """Detailed view of a training plan"""

    model = Training
    redirect_field_name = reverse_lazy("training-update")


class DeleteTrainingView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """A view that lets you delete a single training"""

    model = Training
    success_url = reverse_lazy("training-list")
    success_message = "Usunięto trening!"


class AddTrainingPlanView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Implements a form that adds a training plan to database"""

    model = TrainingPlan
    success_url = reverse_lazy("main-page")
    form_class = TrainingPlanForm
    success_message = "Dodano plan treningowy!"


class TrainingPlanListView(LoginRequiredMixin, ListView):
    """List view of all training plans"""

    model = TrainingPlan
    context_object_name = "training_plan_list"
    template_name = "trainingplan_list.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return TrainingPlan.objects.filter(name__icontains=query)
        else:
            return TrainingPlan.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["object_list"] = TrainingPlan.objects.filter(
            user_id=self.request.user.id
        )
        if self.request.user.is_superuser:
            context["object_list"] = TrainingPlan.objects.all()
        return context


class TrainingPlanDetailView(LoginRequiredMixin, DetailView):
    """Details of a single training plan"""

    model = TrainingPlan
    template_name_suffix = "_update_form"


class UpdateTrainingPlanView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """A view that lets you update a training plan"""

    model = TrainingPlan
    template_name_suffix = "_update_form"
    form_class = TrainingPlanForm
    success_url = reverse_lazy("training-plan-list")
    success_message = "Zaktualizowano plan treningowy!"


class DeleteTrainingPlanView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """A view that lets you delete a single training plan"""

    model = TrainingPlan
    success_url = reverse_lazy("training-plan-list")
    success_message = "Usunięto plan treningowy!"
