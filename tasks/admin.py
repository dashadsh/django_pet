from django.contrib import admin

# Register your models here.

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)

admin.site.register(Task, TaskAdmin)