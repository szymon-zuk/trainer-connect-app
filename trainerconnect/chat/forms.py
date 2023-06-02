from django.forms import ModelForm
from django import forms
from .models import Thread, Message
from django.contrib.auth.models import User


class ThreadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Thread
        fields = "__all__"
        labels = {
            "name": "Nazwa",
            "trainer_id": "Trener",
            "trainee_id": "Podopieczny",
            "description": "Opis",
        }


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Message
        exclude = ["created", "username"]
        labels = {
            "text": "Treść",
            "thread": "Konwersacja",
        }
