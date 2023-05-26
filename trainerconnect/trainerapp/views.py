from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Exercise, Training, TrainingPlan
from .forms import ExerciseForm, TrainingForm, TrainingPlanForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MainPage(View):
    """View of the default page"""

    def get(self, request):
        return render(request, "main_page.html")


class AddExerciseView(LoginRequiredMixin, CreateView):
    """Implements a form that adds an exercise to database"""

    model = Exercise
    success_url = reverse_lazy("main-page")
    form_class = ExerciseForm
    redirect_field_name = reverse_lazy('add-exercise')

    def form_valid(self, form: ExerciseForm):
        messages.success(self.request, "Dodano ćwiczenie!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))


class ExerciseListView(LoginRequiredMixin, ListView):
    """Shows a list of all exercises"""

    model = Exercise
    paginate_by = 30
    redirect_field_name = reverse_lazy('exercise-list')

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Exercise.objects.filter(name__icontains=query)
        else:
            return Exercise.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class UpdateExerciseView(LoginRequiredMixin, UpdateView):
    """A view that lets you update the properties of an exercise"""

    model = Exercise
    fields = {
        "name",
        "sets",
        "reps",
        "load",
        "comment"
    }
    success_url = reverse_lazy("exercise-list")
    redirect_field_name = reverse_lazy('update-exercise')

    def form_valid(self, form: ExerciseForm):
        messages.success(self.request, "Zaktualizowano ćwiczenie!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))


class DeleteExerciseView(DeleteView):
    """A view that lets you delete a single exercise"""

    model = Exercise
    success_url = reverse_lazy("exercise-list")
    success_message = "Usunięto ćwiczenie!"
    
    def get_success_message(self, cleaned_data):
        return f"Usunięto ćwiczenie {cleaned_data['name']}"


class AddTrainingView(CreateView):
    """Implements a form that adds a training to database"""

    model = Training
    success_url = reverse_lazy("main-page")
    form_class = TrainingForm

    def form_valid(self, form: TrainingForm):
        messages.success(self.request, "Dodano trening!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))


class TrainingListView(ListView):
    """List view of all trainings"""
    model = Training
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Training.objects.filter(name__icontains=query)
        else:
            return Training.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class UpdateTrainingView(UpdateView):
    model = Training
    fields = {
        "name",
        "description",
        "exercises",
    }
    success_url = reverse_lazy("training-list")

    def form_valid(self, form: TrainingForm):
        messages.success(self.request, "Zaktualizowano trening!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTrainingView(DeleteView):
    """A view that lets you delete a single training"""

    model = Training
    success_url = reverse_lazy("training-list")
    success_message = "Usunięto trening!"
    
    def get_success_message(self, cleaned_data):
        return f"Usunięto trening {cleaned_data['name']}"


class AddTrainingPlanView(CreateView):
    """Implements a form that adds a training plan to database"""
    model = TrainingPlan
    success_url = reverse_lazy("main-page")
    form_class = TrainingPlanForm

    def form_valid(self, form: TrainingPlanForm):
        messages.success(self.request, "Dodano plan treningowy!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))



class TrainingPlanListView(ListView):
    """List view of all training plans"""

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


class UpdateTrainingPlanView(UpdateView):
    """A view that lets you update a training plan"""

    model = TrainingPlan
    fields = {
        "name",
        "description",
        "trainings",
        "user_id"
    }
    success_url = reverse_lazy("training-plan-list")
    
    def form_valid(self, form: TrainingPlanForm):
        messages.success(self.request, "Zaktualizowano plan treningowy!")
        form.save()
        return self.render_to_response(self.get_context_data(form=form))
    
    
class DeleteTrainingPlanView(DeleteView):
    """A view that lets you delete a single training plan"""

    model = TrainingPlan
    success_url = reverse_lazy("training-plan-list")
    success_message = "Usunięto plan treningowy!"
    
    def get_success_message(self, cleaned_data):
        return f"Usunięto trening {cleaned_data['name']}"
