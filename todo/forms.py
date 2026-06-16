from django.forms import ModelForm
from .models import TodoList


class TodoForm(ModelForm):
	class Meta:
		model = TodoList
		fields = ['title', 'priority', 'description', 'due_date', 'status']


		labels= {
			'title':'عنوان',
			'priority':'اولویت',
			'description':'توضیحات',
			'due_date':'تاریخ انجام',
			'status':'وضعیت',
		}