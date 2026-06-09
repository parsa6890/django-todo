from django.urls import path
from . import views


urlpatterns = [
	path('', views.todo_view, name='todos'),
	path('creat_task/', views.creat_task_view, name='creat_task'),
	path('delete_task/<int:id>/', views.delete_task_view, name='delete_task'),
	path('edit_task/<int:id>/', views.edit_task_view, name='edit_task'),
]