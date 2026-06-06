from django.shortcuts import render
from django.http import HttpResponse

def  test(request):
	return HttpResponse('hello this is the test view from todo app')
