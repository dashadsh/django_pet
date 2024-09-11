from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# we have to create a view function that will be called when the URL is visited
def list_todo_items(request):
	return HttpResponse('You are seeing HttpResponse from list_todo_items view.')

# when i open the URL http://127.0.0.1:8000/todos/list/ in the browser, the view function will be called
# and the HttpResponse will be returned to the browser:
# from list_todo_items view