# To-Do List Application
This is a simple To-Do List web application built with Django, PostgreSQL, and Bootstrap.

## Features

- View a list of tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks

## Prerequisites

- Python 3.8 or above
- PostgreSQL

## Setup

	**create a virtual environment (optional):** 
    ```bash
    python -m venv myenv
	source myenv/bin/activate 
    ```

	**deactivate:** 
	```bash
    deactivate 
    ```
	# Install Django, psycopg2, and Bootstrap 
pip install django psycopg2-binary

	# Create a Django Project
django-admin startproject todolist_project
cd todolist_project

	# Create a Django App
python3 manage.py startapp tasks

	# Test it
	# navigate to project folder
cd todolist_project
python3 manage.py runserver
	# check in browser
python3 manage.py showmigrations

################################################
##### Configure PostgreSQL Database

	# Install PostgreSQL and Create a Database
brew install postgresql
brew services start postgresql

	# Connect to a db with the same name as the current system user
psql postgres

	# Create db
CREATE DATABASE todolist_db;
CREATE USER todolist_user WITH PASSWORD 'yourpassword';
ALTER ROLE todolist_user SET client_encoding TO 'utf8';
ALTER ROLE todolist_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE todolist_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE todolist_db TO todolist_user;
\q

	# Edit todolist_project/settings.py to configure PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist_db',
        'USER': 'todolist_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

	# Update tasks/models.py - create Models
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
	
	# Verify the App is Included in INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Ensure this line is included
]

	# create & apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

	# To Test from browser (ensure the model is registered with the admin site)
python3 manage.py createsuperuser
python3 manage.py runserver
	# go to http://127.0.0.1:8000/admin/


	# Test db
python3 manage.py shell
from tasks.models import Task
print(Task.objects.all())

##########################  Create Views and Templates 
	# UPD tasks/views.py (see its concent)

	# create tasks/forms.py
	# create the following HTML files in tasks/templates/tasks/:

task_list.html add_task.html
