from .models import Exercise, Training, TrainingPlan
from django import forms


class ExerciseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Exercise
        fields = ["name", "sets", "reps", "load", "comment"]
        labels = {
            "name": "Nazwa ćwiczenia",
            "sets": "Ilość serii",
            "reps": "Ilość powtórzeń",
            "load": "Ciężar",
            "comment": "Komentarz",
        }


class TrainingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Training
        fields = ["name", "description", "exercises"]
        labels = {
            "name": "Nazwa treningu",
            "description": "Opis",
            "exercises": "Ćwiczenia",
        }


class TrainingPlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainingPlanForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = TrainingPlan
        fields = ["name", "description", "trainings", "user_id"]
        labels = {
            "name": "Nazwa planu",
            "description": "Opis",
            "trainings": "Treningi",
            "user_id": "Użytkownik",
        }
