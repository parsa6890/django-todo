from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm


STATUS_CHOICES = ['pending', 'in_progress', 'done']
def todo_view(request):
	all_list = TodoList.objects.all()
	grouped_todos = {
		status : all_list.filter(status=status)
				for status in STATUS_CHOICES
	}
	context={
		'grouped_todos': grouped_todos
	}
	return render(request, 'todo/index.html', context)


def cform_view(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todos')
	else:
		form= TodoForm()
	context= {
		"form" : form
	}
	return render(request, 'todo/creat_task.html', context)


def delete_task(request, id):
	task = get_object_or_404(TodoList, id= id)
	task.delete()
	return redirect('todos')


