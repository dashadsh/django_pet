from django.contrib import admin

# Register your models here.
from .models import Task

# The ORM is integrated with Django's admin interface through tasks/admin.py:
class TaskAdmin(admin.ModelAdmin):
	# Tuple defines the fields that will be displayed in the list view of the admin interface.
    list_display = ('title', 'completed')

	# Tuple specifies the fields that can be searched using the search box in the admin interface.
    # Users can search tasks by their title.
    search_fields = ('title',)

	# Tuple defines the fields by which the task list can be filtered in the admin interface.
    list_filter = ('completed',)

admin.site.register(Task, TaskAdmin)