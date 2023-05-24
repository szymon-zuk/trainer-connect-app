from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Thread


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
    context_object_name = "thread_list"
    form_class = ThreadForm
    success_message = "Dodano konwersację!"

    def get_success_message(self, cleaned_data):
        return f"Dodano konwersację z {cleaned_data['trainee_id']}"
