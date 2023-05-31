from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Thread, Message
from .forms import ThreadForm, MessageForm


class ThreadListView(LoginRequiredMixin, ListView):
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
        context["thread_list"] = Thread.objects.filter(
            trainee_id=self.request.user.id
        )
        if self.request.user.is_superuser:
            context["thread_list"] = Thread.objects.all()
        context['message_list'] = Message.objects.all()
        return context


class AddThreadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View of adding a thread"""

    model = Thread
    success_url = reverse_lazy("thread-list")
    form_class = ThreadForm
    success_message = "Dodano konwersację!"


class AddMessageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View of adding a message"""
    model = Message
    form_class = MessageForm
    success_message = "Dodano wiadomość!"

    def get_success_url(self):
        return reverse_lazy('thread-list')


class ThreadDetailView(LoginRequiredMixin, DetailView):
    """Single thread view which displays all the messages in a thread"""
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_list'] = Message.objects.filter(thread_id=self.kwargs['pk'])
        return context


class DeleteMessageView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """Deleting message from db"""
    model = Message
    success_message = "Usunięto wiadomość"
    success_url = reverse_lazy("thread-list")


class DeleteThreadView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """Deleting a single thread from db"""
    model = Thread
    success_message = "Usunięto konwersację"
    success_url = reverse_lazy("thread-list")
