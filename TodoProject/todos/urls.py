from django.urls import path
from . import views
# we have to import the view function that we created in the views.py file

urlpatterns = [
	path('list/', views.list_todo_items),
]

# we have to map the URL to a view function inside the todos app