# Django Todo Application with PostgreSQL

This is a step-by-step guide for beginners to create a simple Django web application using PostgreSQL as the database and Bootstrap for front-end styling.

## Project Prerequisites

Before starting, ensure you have the following installed:

- **Python**: Programming language.
- **pip**: Python package installer.
- **PostgreSQL**: Database system.
- **psycopg2-binary**: PostgreSQL database adapter for Python.

## 1. Create the Django Project

1. Start a new Django project:

    ```bash
    django-admin startproject TodoProject
    cd TodoProject
    ```

2. Test the initial setup by running the development server:

    ```bash
    python3 manage.py runserver
    ```

    You should see the default Django welcome page at `http://127.0.0.1:8000/`.


## 2. Project Structure

The parent TodoProject folder contains another folder with the same name, which in turn contains the main Python configuration files.

We can have as many applications as we need. In this project, I'm creating a new app called "todos."

Project will have the following structure:

	```bash
	● TodoProject
	|
	+---● todos (app folder)
	|   |
	|   +--● migrations (includes files related to migrations)
	|   | 
	|   +--● static
	|   |  |--● todos
	|   |  |  |--styles.css
	|   |  
	|   +--● templates
	|   |  |--● todos
	|   |  |  |--todo_list.html
	|   | 
	|   |-- models.py (python class for each database table)
	|   |-- urls.py (app. specific url mapping)
	|   |-- views.py (view fns. to handle http request)
	|
	+---● TodoProject
	|   |
	|   |--setting.py (project config. file)
	|   |--urls.py (url mapping for the project)
	```

## 3. Create a Django App

1. Create a new app called `todos`:

    ```bash
    python3 manage.py startapp todos
    ```

2. Register the new app in the `INSTALLED_APPS` section of `TodoProject/settings.py`:

    ```python
    INSTALLED_APPS = [
        # Default Django apps
        'todos',  # New app
    ]
    ```

## 4. Set Up PostgreSQL Database

**Object-Relational-Mapping (ORM) Frameworks:**\
.NET - Entity Framework\
PHP - CakePHP\
Python - Django\
\
Django already supports Object-Relational Mapping (ORM). Using Python classes, we can create database tables, which are referred to as "models."\
\
Class: Represents a database table.
Properties (inside the class): Represent table columns.\
The ORM framework automates the migrations process, where models are translated into physical database tables.\
\
ORMs also allow you to manipulate the database using object-oriented code, instead of writing raw SQL queries.\

1. Install PostgreSQL (if you don't have it):

    ```bash
	psql --version // OR brew list | grep postgresql
    brew install postgresql
    brew services start postgresql
    ```

2. Create the database and user:

    ```bash
    psql postgres
    ```

    Run the following commands inside the PostgreSQL shell:

    ```sql
    CREATE DATABASE tododb;
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ALTER ROLE myuser SET client_encoding TO 'utf8';
    ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE tododb TO myuser;
    \q
    ```

3. Test if DB is there:
    ```bash
    psql postgres
	\l
    ```
DROP DATABASE "dbname";  can be used to delete database. Postgres, template0, and template1 are system databases and should not be deleted. 

4. Test users:
    ```bash
    psql postgres
	\du
    ```

5. If encountering issues:
    ```bash
	sudo su
	adduser postgres
	usermod -aG sudo postgres
	exit
	sudo -u postgres psql OR psql -U postgres
    ```

## 5. Configure Django to Use PostgreSQL

Open `TodoProject/settings.py` and update the `DATABASES` setting:

    ```bash
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tododb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '',  # Leave blank for default
	```

## 6. Define Models and Migrate Database

1. Define a Todo model inside todos/models.py:

    ```bash
	from django.db import models

	class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    ```

2. Create migrations for the new model:
    ```bash
	python3 manage.py makemigrations todos
	````

Expected output:
    ```bash
	Migrations for 'todos':
	todos/migrations/0001_initial.py
	Create model Todo
    ```

3. Check the SQL commands that will be executed for the migration:
	```bash
	python3 manage.py sqlmigrate todos 0001
	```
This command generates and displays the SQL queries that will be run for the migration, which is useful for debugging and inspection.

4. Apply the migrations:
	```bash
	python3 manage.py migrate
	````

# 7. Verify Database and Migrations

1. List the applied migrations:
	```bash
	python3 manage.py showmigrations todos
	```
2. To interact with the database directly, open the PostgreSQL shell and list the tables:
	```bash
	psql tododb
	\dt
	```
3. To describe the schema of the todos_todo table:
	```bash
	\d todos_todo
	```
4. Query the todos_todo table:
	```bash
	SELECT * FROM todos_todo;
	```

# 8. Configure Routing

1. Create a todos/urls.py file for app-specific URL mappings:
	```bash
	from django.urls import path, include
	urlpatterns = [
		# existing admin path
		path('todos/', include('todos.urls')),
	]
	```

2. Modify the main TodoProject/urls.py to include the todos app URLs:
	```bash
	from djando.urls import path
	from . import views

	urlpatterns = [
		path('list/', views.list_todo_items),
	]
	```

# 9. Create a Simple View

1. In todos/views.py, create a simple view to display a message:
	```bash
	from django.http import HttpResponse
	def list_todo_items(request):
		return HttpResponse('You are seeing HttpResponse from list_todo_items view.')
	```

# 10. Create template

1. Create templates/todos/todo_list.html as stated in 00.html:
	```bash
		<!DOCTYPE html>
	<html lang="en">
	<head>
		<!-- Meta tags for character set and viewport -->
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>To-Do List</title>
	</head>
	<body>

	</body>
	</html>
	```
Check out 01.html and 02.html.

2. Modify views.py by encluding new response:
	```bash
	def list_todo_items(request):
		return render(request, 'todos/02.html')
	```




