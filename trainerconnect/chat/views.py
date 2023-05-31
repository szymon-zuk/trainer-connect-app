from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Thread, Message
from .forms import ThreadForm, MessageForm
from django.contrib import messages


class ThreadListView(ListView):
    """List view of all threads - trainee only sees one, and trainer sees all of them"""

    model = Thread
    paginate_by = 20
    context_object_name = "thread_list"
    template_name = "thread_list.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return Thread.objects.filter(name__icontains=query)
        else:
            return Thread.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["object_list"] = Thread.objects.filter(
            user_id=self.request.user.id
        )
        if self.request.user.is_superuser:
            context["object_list"] = Thread.objects.all()
        return context


class AddThreadView(SuccessMessageMixin, CreateView):
    """View of adding a thread"""

    model = Thread
    success_url = reverse_lazy("thread-list")
    form_class = ThreadForm
    success_message = "Dodano konwersację!"



class AddMessageView(SuccessMessageMixin, CreateView):
    model = Message
    success_url = reverse_lazy("message-list")
    form_class = MessageForm
    success_message = "Dodano wiadomość!"


class ThreadDetailView(DetailView):
    model = Thread
    context_object_name = "message_list"

