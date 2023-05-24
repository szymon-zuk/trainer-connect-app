from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Thread, Message
from .forms import ThreadForm


class ThreadView(ListView):
    """List view of all threads - trainee only sees one, and trainer sees all of them"""
    model = Thread
    paginate_by = 20
    context_object_name = 'thread_list'
    template_name = "thread_list.html"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Thread.objects.filter(name__icontains=query)
        else:
            return Thread.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class AddThreadView(CreateView):
    """View of adding a thread"""
    model = Thread
    success_url = "thread-list"
    form_class = ThreadForm
    
    def form_valid(self, form: ThreadForm) -> HttpResponse:
        messages.success(self.request, "Dodano konwersację!")
        return self.render_to_response(self.get_context_data(form=form))

class AddMessageView(CreateView):
    model = Message
    success_url = "message-list"
    form_class = MessageForm

    def form_valid(self, form: MessageForm) -> HttpResponse:
        messages.success(self.request, "Wysłano wiadomość!")
        return self.render_to_response(self.get_context_data(form=form))