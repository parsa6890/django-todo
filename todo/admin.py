from django.contrib import admin
from .models import TodoList, Conversation, Message


admin.site.register(TodoList)
admin.site.register(Conversation)
admin.site.register(Message)