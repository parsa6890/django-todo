from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import TodoList
from .forms import TodoForm
from django.contrib import messages


STATUS_CHOICES=['pending', 'in_progress', 'done']
def todo_view(request):
	all_list=TodoList.objects.all()
	grouped_todos={
		status: all_list.filter(status=status)
				for status in STATUS_CHOICES
	}
	context={
		'grouped_todos': grouped_todos
	}
	return render(request, 'todo/index.html', context)


def creat_task_view(request):
	if request.method=="POST":
		form=TodoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "وظیفه جدید با موفقیت ایجاد شد.")
			return redirect('todos')
	else:
		form=TodoForm()
	context={
		"form":form
	}
	return render(request, 'todo/creat_task.html', context)


def delete_task_view(request, id):
	task=get_object_or_404(TodoList, id= id)
	task.delete()
	messages.success(request, "وظیفه مورد نظر شما با موفقیت حذف شد.")
	return redirect('todos')



def edit_task_view(request, id):
	task=get_object_or_404(TodoList, id= id)
	if request.method=="POST":
		form=TodoForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.success(request, "وظیفه مورد نظر شما با موفقیت ویرایش شد.")	
			return redirect('todos')
	else:
		form=TodoForm(instance=task)
	context={
		"form":form
	}
	return render(request, 'todo/edit_task.html', context)


def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("todos")
		else:
			return render(request, "todo/login.html", {"error": "اطلاعات وارد شده صحیح نمی باشد"})
	return render(request, "todo/login.html")


def logout_view(request):
	logout(request)
	return redirect("login")