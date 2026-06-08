from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList


STATUS_CHOICES = ['pending', 'in_progress', 'done']

def todo_view(request):
	all_list = TodoList.objects.all()
	# pending_list= TodoList.objects.filter(status='pending')
	# inprogress_list= TodoList.objects.filter(status='in_progress')
	# done_list= TodoList.objects.filter(status='done')
	grouped_todos = {
		status : all_list.filter(status=status)
				for status in STATUS_CHOICES
	}
	context={
		# 'all_list': all_list,
		# 'pending_list': pending_list,
		# 'inprogress_list': inprogress_list,
		# 'done_list': done_list,
		'grouped_todos': grouped_todos
	}
	return render(request, 'todo/index.html', context)

