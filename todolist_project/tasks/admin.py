from django.contrib import admin

# Register your models here.
# This file is where you register models with the Django admin interface. 
# You need to import your model and register it.

###### NEW ######
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): #  Inherits from admin.ModelAdmin, which is a class that defines the behavior of the admin interface.
    list_display = ('title', 'completed') #  Specifies which fields to display in the list view.
    list_filter = ('completed',) #  Specifies which fields to use for filtering the list view.
    search_fields = ('title',) # Specifies which fields to use for searching the list view.

###### NEW ######
