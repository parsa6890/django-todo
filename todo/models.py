from django.db import models
from django.contrib.auth.models import User



PRIORITY_LOW = 1
PRIORITY_MEDIUM = 2
PRIORITY_HIGH = 3

PRIORITY_CHOICES = [
	(PRIORITY_LOW, 'پایین'),
	(PRIORITY_MEDIUM, 'متوسط'),
	(PRIORITY_HIGH, 'بالا'),
]

STATUS_PENDING = 'pending'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_DONE = 'done'

STATUS_CHOICES = [
	(STATUS_PENDING, 'در حال بررسی'),
	(STATUS_IN_PROGRESS, 'در حال انجام'),
	(STATUS_DONE, 'انجام شده'),
]

class TodoList(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 255)
	priority = models.IntegerField(choices=PRIORITY_CHOICES,default=PRIORITY_MEDIUM)
	description = models.TextField(blank = True)
	due_date = models.DateTimeField(null= True, blank= True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title
	

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(upload_to="profile_images/", blank=True)
	email= models.EmailField(blank=True)
	organizational_email= models.EmailField(blank=True)
	mobile = models.CharField(max_length=12, blank=True)
	internal_number = models.CharField(max_length=5, blank=True)
	bio = models.TextField(max_length=255, blank=True)