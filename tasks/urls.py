from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),  # Home page: list tasks
    path('add/', TaskCreateView.as_view(), name='add_task'),  # Add a new task
    path('complete/<int:pk>/', TaskUpdateView.as_view(), name='complete_task'),  # Mark task as completed
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),  # Delete a task
]
