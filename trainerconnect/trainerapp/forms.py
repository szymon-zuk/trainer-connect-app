from .models import Exercise, Training
from django.forms import ModelForm
from django import forms

# rozważyć użycie django-crispy-forms do stylowania formularzy


class ExerciseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'load', 'comment']


class TrainingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Training
        fields = ['name', 'description', 'exercises']