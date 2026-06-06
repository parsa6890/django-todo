from django.db import models



PRIORITY_LOW = 1
PRIORITY_MEDIUM = 2
PRIORITY_HIGH = 3

PRIORITY_CHOICES = [
	(PRIORITY_LOW, 'Low'),
	(PRIORITY_MEDIUM, 'Medium'),
	(PRIORITY_HIGH, 'High'),
]

STATUS_PENDING = 'pending'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_DONE = 'done'

STATUS_CHOICES = [
	(STATUS_PENDING, 'Pending'),
	(STATUS_IN_PROGRESS, 'In Progress'),
	(STATUS_DONE, 'Done'),
]

class TodoList(models.Model):
	title = models.CharField(max_length = 255)
	priority = models.IntegerField(choices=PRIORITY_CHOICES,default=PRIORITY_MEDIUM)
	description = models.TextField(blank = True)
	due_date = models.DateTimeField(null= True, blank= True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	created_at = models.DateTimeField(auto_now_add = True)