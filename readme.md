# To-Do List Application
This is a simple To-Do List web application built with Django, PostgreSQL, and Bootstrap.

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

**Install Django, psycopg2, and Bootstrap**
	```bash 
	pip install django psycopg2-binary
	```

**Create a Django Project**
	```bash
	django-admin startproject todo_project
	cd todo_project
	```

**Create a Django App**
	```bash
	python3 manage.py startapp tasks
	```

**Include the App in INSTALLED_APPS**
	```bash
	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'tasks',  # Ensure this line is included
	]
	```

**Test it**
	```bash
	cd todolist_project
	python3 manage.py runserver
	```

**Test migrations**
	```bash
	python3 manage.py showmigrations
	```

# Configure PostgreSQL Database

**Install PostgreSQL and Create a Database**
	```bash
	brew install postgresql
	brew services start postgresql
	```

**Connect to a db with the same name as the current system user**
	```bash
	psql postgres
	```

**Create db**
	```bash
	CREATE DATABASE mydb;
	CREATE USER mydbuser WITH PASSWORD 'mypassword';
	ALTER ROLE mydbuser SET client_encoding TO 'utf8';
	ALTER ROLE mydbuser SET default_transaction_isolation TO 'read committed';
	ALTER ROLE mydbuser SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE mydb TO mydbuser;
	\q
	```

**Update todolist_project/settings.py to configure PostgreSQL**
	```bash
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME': 'mydb',  # Name of your PostgreSQL database
			'USER': 'mydbuser',   # Your PostgreSQL user
			'PASSWORD': 'mypassword',  # Your PostgreSQL password
			'HOST': 'localhost',
			'PORT': '5432',     # Default PostgreSQL port
		}
	}
	```

**Update tasks/models.py - create Models**
	```bash
	from django.db import models

	class Task(models.Model):
		title = models.CharField(max_length=200)
		completed = models.BooleanField(default=False)

		def __str__(self):
			return self.title
	```
	
**Create admin user**
	```bash
	python3 manage.py createsuperuser
	python3 manage.py runserver
		# go to http://127.0.0.1:8000/admin/
	```

**Register Model with Admin Interface in tasks/admin.py**
See: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
	```bash
	from django.contrib import admin
	from .models import Task

	class TaskAdmin(admin.ModelAdmin):
		list_display = ('title', 'completed')
		search_fields = ('title',)
		list_filter = ('completed',)

	admin.site.register(Task, TaskAdmin)
	```

**Create & apply migrations**
Migrations in Django are a way of propagating changes you make to your models (like adding or modifying fields) into the database schema.
	```bash
	python3 manage.py makemigrations
	python3 manage.py migrate
	```
If you need to undo changes, you can roll back migrations to a previous state.
	```bash
	python3 manage.py migrate myapp 0001
	```


**Verify db**
Django's ORM handles the translation of Python code to SQL queries and vice versa.
	```bash
	python3 manage.py shell
	from tasks.models import Task
	print(Task.objects.all())
	```

**Create Views and Templates**
Update tasks/views.py\
Views handle the logic for processing requests, interacting with the data, and returning responses to the client.\
We are using Class Based Views, see:\
https://www.makeuseof.com/crud-app-with-django-class-based-views/\
https://docs.djangoproject.com/en/4.2/topics/class-based-views/\

\
Update todolist_project/urls.py\
\
Create Templates at tasks/templates/tasks/\

**Expected project structure**
	```bash
		todolist_project/
	├── todolist_project/
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
