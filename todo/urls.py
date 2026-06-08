from django.urls import path
from . import views


urlpatterns = [
	path('', views.todo_view, name='todos'),
	path('creat_task/', views.cform_view, name='creat_task'),
]