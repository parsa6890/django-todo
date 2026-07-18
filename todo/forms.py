from django.forms import ModelForm
from .models import TodoList, UserProfile
from django.contrib.auth.models import User


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


class UserProfileForm(ModelForm):
	class Meta:
		model= UserProfile
		fields= ['profile_image','email','organizational_email','mobile','internal_number','bio']

		labels= {
			'profile_image':'عکس پروفایل',
			'email':'ایمیل',
			'organizational_email':'ایمیل سازمانی',
			'mobile':'موبایل',
			'internal_number':'داخلی',
			'bio':'درباره من',
		}


class UserForm(ModelForm):
	class Meta:
		model= User
		fields= ['username', 'first_name', 'last_name']

		labels= {
			'username':'نام کاربری',
			'first_name':'نام',
			'last_name':'نام خانوادگی',
		}