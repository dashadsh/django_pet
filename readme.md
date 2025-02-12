# README.md

# To-Do List Application

A simple To-Do List web application built with Django, PostgreSQL, and Bootstrap.

## Features
- View a list of tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks

## Prerequisites
- Python 3.8 or above
- pip
- PostgreSQL - relational database
- psycopg2-binary

# Initial Setup

## 1. Python Environment
```bash
# Create and activate virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install required packages
pip install django psycopg2-binary
```

## 2. PostgreSQL Setup
```bash
# Install PostgreSQL (macOS)
brew install postgresql
brew services start postgresql

# Connect to PostgreSQL
psql postgres

# Create database and user
CREATE DATABASE mydb;
CREATE USER mydbuser WITH PASSWORD 'mypassword';
ALTER ROLE mydbuser SET client_encoding TO 'utf8';
ALTER ROLE mydbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydbuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydb TO mydbuser;
\q
```

## 3. Project Creation
```bash
# Create Django project and app
django-admin startproject todo_project
cd todo_project
python3 manage.py startapp tasks
```

## 4. Configuration

### Add App to INSTALLED_APPS (settings.py)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Add this line
]
```

### Configure Database (settings.py)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'mydbuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 5. Create Models (tasks/models.py)
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## 6. Set Up Admin Interface (tasks/admin.py)
```python
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)

admin.site.register(Task, TaskAdmin)
```

## 7. Database Setup
```bash
# Create and apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create admin user
python3 manage.py createsuperuser
```

# Usage Instructions

## Running the Application
```bash
# Make sure you're in the directory containing manage.py
cd todo_project
python3 manage.py runserver
```
Access the application at: http://127.0.0.1:8000/
Access the admin interface at: http://127.0.0.1:8000/admin/

## Development Commands

### Virtual Environment
```bash
# Activate virtual environment
source myenv/bin/activate

# Deactivate when done
deactivate
```

### Database Management
```bash
# Check migration status (in 2nd terminal activate venv and navigate to project folder)
python3 manage.py showmigrations

# Roll back migrations (if needed)
python3 manage.py migrate tasks 0001

# Verify database (Django shell)
python3 manage.py shell
from tasks.models import Task
print(Task.objects.all())
```

## Creating Views and Templates
- Update tasks/views.py - handles logic for processing requests
- Update todo_project/urls.py
- Create templates in tasks/templates/tasks/

We are using Class Based Views, see:
- https://www.makeuseof.com/crud-app-with-django-class-based-views/
- https://docs.djangoproject.com/en/4.2/topics/class-based-views/
- Admin Interface Documentation: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/

## Project Structure
```
todo_project/
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── tasks/
│           ├── add_task.html
│           ├── task_confirm_delete.html
│           ├── task_form.html
│           └── task_list.html
├── manage.py
└── requirements.txt
```

## Notes
- Django's ORM handles the translation of Python code to SQL queries and vice versa
- Migrations propagate model changes to the database schema
- Always run manage.py commands from the directory containing manage.py
- Use a second terminal for migrations while the server is running