from django.shortcuts import render, redirect # add redirect !!!

# Create your views here.
######## NEW ########
from .models import Task #  Import the Task model from the models.py file.
from .forms import TaskForm #  Import the TaskForm from the forms.py file. - NEW

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list') # Redirect to the task list view
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def mark_completed(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')
######## NEW ########
# Views are Python functions that take a web request and return a web response.