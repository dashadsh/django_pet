from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Task

# List all tasks
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

# Create a new task
class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title']
    success_url = reverse_lazy('task_list')

# Mark task as completed (UpdateView)
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['completed']
    success_url = reverse_lazy('task_list')

    # Automatically mark task as completed
    def form_valid(self, form):
        form.instance.completed = True
        return super().form_valid(form)

# Delete a task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
