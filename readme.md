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

TodoProject/ │ ├── TodoProject/ │ ├── init.py │ ├── settings.py # Project configuration file │ ├── urls.py # Routing and URL mapping │ └── wsgi.py │ ├── todos/ # New app for To-Do items │ ├── migrations/ # Auto-generated database migration files │ ├── static/ # Static files like CSS/JS │ │ └── todos/ │ │ └── styles.css │ ├── templates/ # HTML templates │ │ └── todos/ │ │ └── todo_list.html │ ├── models.py # Database models (tables) │ ├── urls.py # App-specific URL mapping │ └── views.py # Views to handle HTTP requests └── manage.py

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

**Object-Relational-Mapping (ORM) Frameworks:**/
.NET - Entity Framework/
PHP - CakePHP/
Python - Django/
/
Django already supports Object-Relational Mapping (ORM). Using Python classes, we can create database tables, which are referred to as "models."/
/
Class: Represents a database table.
Properties (inside the class): Represent table columns./
The ORM framework automates the migrations process, where models are translated into physical database tables./
/
ORMs also allow you to manipulate the database using object-oriented code, instead of writing raw SQL queries./

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

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tododb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '',  # Leave blank for default
    }
}

## 6. Define Models and Migrate Database

**Do migrations (see other applications in settings.py, their models will be added too)**
python3 manage.py makemigrations todos
# Expected output:
# Migrations for 'todos':
#  todos/migrations/0001_initial.py
#    - Create model Todo

python3 manage.py sqlmigrate todos 0001
# The command generates and displays the SQL commands that will be executed for the specified migration. Used for debugging, inspection purposes.
python3 manage.py migrate

# We can simply execute last command if we want to apply default settings

**Test it**
# List applied migrations
python3 manage.py showmigrations todos
# Access DB
psql tododb
# List tables
\qt
# Describe table schema
\d todos_todo
# Query the table
SELECT * FROM todos_todo;

**Configure routing for the app in urls.py**
# Create todos/urls.py
# Modify urls.py, add path to newly created file to main urls.py
from django.urls import path, include
urlpatterns = [
    # existing admin path
	path('todos/', include('todos.urls')),
]
# Modify todos/urls.py:
from djando.urls import path
from . import views

urlpatterns = [
	path('list/', views.list_todo_items),
]

# Modify todos/views.py
from django.http import HttpResponse
def list_todo_items(request):
	return HttpResponse('You are seeing HttpResponse from list_todo_items view.')
