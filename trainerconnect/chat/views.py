from django.shortcuts import render, redirect
from django.views import View


class ChatView(View):
    """Basic chat view"""
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'chat.html')