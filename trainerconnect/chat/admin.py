from django.contrib import admin
from chat.models import Message, Thread


admin.site.register(Message)
admin.site.register(Thread)