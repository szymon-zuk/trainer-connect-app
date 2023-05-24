from django.forms import ModelForm
from django import forms

class ThreadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Thread
        fields = ["thread_name", "trainer_id", "trainee_id", "description"]
        labels = {
            "name": "Nazwa",
            "trainer_id": "Trener",
            "trainee_id": "Podopieczny",
            "description": "Opis",
        }