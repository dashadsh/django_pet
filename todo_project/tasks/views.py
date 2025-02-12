from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

# We are using Django's class-based views to create the views for our tasks app.
# Alternatively, we could have used function-based views.
# https://www.makeuseof.com/crud-app-with-django-class-based-views/

# View to list all tasks
class TaskListView(ListView):
    model = Task  # The model to use for this view
    context_object_name = 'tasks'  # Name of the context variable in the template
    template_name = 'tasks/task_list.html'  # Specify the template to use

# View to create a new task
class TaskCreateView(CreateView):
    model = Task  # The model to use for this view
    fields = ['title']  # Fields to include in the form
    success_url = reverse_lazy('task_list')  # URL to redirect to after finishing the task
    template_name = 'tasks/task_form.html'  # Specify the template to use

# View to update a task
class TaskUpdateView(UpdateView):
    model = Task  # The model to use for this view
    fields = ['completed']  # Fields to include in the form
    success_url = reverse_lazy('task_list')  # URL to redirect to after finishing the task
    template_name = 'tasks/task_update_form.html'  # Specify the template to use

    # Override to automatically mark the task as completed
    def form_valid(self, form):
        print(f"Updating task ID {form.instance.pk} to completed.")
        form.instance.completed = True  # Set the completed field to True
        return super().form_valid(form)  # Call the parent method to save

# View to delete a task
class TaskDeleteView(DeleteView):
    model = Task  # The model to use for this view
    success_url = reverse_lazy('task_list')  # URL to redirect to after deleting the task
    template_name = 'tasks/task_confirm_delete.html'  # Specify the template to use


# NAMING CONVENTION FOR TEMPLATES
# Django has a naming convention for templates that are used with class-based views.
# The template name should be <app_name>/<model_name>_<view_type>.html
# For example, the template for TaskListView should be tasks/task_list.html.
# In this case, Django will automatically look for a template named tasks/task_list.html.

# URL NAME RESOLUTION
# The reverse_lazy function is used to reverse URL names in class-based views
# (similar to the reverse function in function-based views).
# When we write reverse_lazy('task_list'), 
# Django will look for a URL pattern in the urls.py with the name 'task_list':
# path('', TaskListView.as_view(), name='task_list')

# CONTEXT VARIABLES
# The context_object_name attribute is used to specify the name of the context variable that will be used in the template.
# In this case, we are setting context_object_name = 'tasks',
# which makes the list of tasks available in the template as tasks.
# {% for task in tasks %} : Loop through all Task objects in the database
# 	{{ task.title }} : display the title of each task
# 	{{ task.completed }} : display the completion status of each task
# {% url 'complete_task' task.id %} : generate the URL for the complete_task view with the task's id as a parameter

# PRIMARY KEY
# The primary key (pk) is a unique identifier for each record in the database.
# <int:pk> is conceptually the same as task.id in the context of Django URLs and model instances.

# AJAX
# If you want to mark a task as completed without redirecting to a separate page
# and instead update the main page directly, you can achieve this using AJAX 
# (Asynchronous JavaScript and XML) to send the update request in the background. 
# This allows you to update the task status without reloading or navigating away 
# from the current page.