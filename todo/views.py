from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList


def todo_view(request):
	todo_list = TodoList.objects.all()
	pending_list= todo_list.filter(status='pending')
	done_list= todo_list.filter(status='done')
	context={
		'pending_list': pending_list,
		'done_list': done_list,
	}
	return render(request, 'todo/index.html', context)

