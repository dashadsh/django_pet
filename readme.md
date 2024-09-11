This is a step-by-step guide for beginners to create a simple Django web application using PostgreSQL and the Bootstrap toolkit.

**Project prerequisites:**
python
pip
postgresql
psycopg2-binary (PostgreSQL database adapter for Python)

**Create project**
django-admin startproject TodoProject
cd TodoProject 

**Test init setup - run development server, see how default django works**
python3 manage.py runserver

**Project structure**
Parent TodoProject folder contains another folder with the same name, 
which respectively contains main python configiration files.

We can have as many applycations as we need.
In this project I'm creating a new app called "todos".

TodoProject
|
|---- TodoProject
|    |
|    |--setting.py (project configuration file)
|    |--urls.py (routing/url mapping for the project)
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


**Create an app (from parent directory)**
python3 manage.py startapp todos

**Tell the preject, we created new app, in settings.py**
INSTALLED_APPS = [
    # Other Django apps
    'todos',
]

**Object-Relational-Mapping  ORM**
ORM Frameworks
.NET - Entity Framework
PHP - CakePHP
Python - Django

Django already supports Object-Relational Mapping (ORM). Using Python classes, we can create database tables, which are referred to as "models."

Class: Represents a database table.
Properties (inside the class): Represent table columns.
The ORM framework automates the migrations process, where models are translated into physical database tables.

ORMs also allow you to manipulate the database using object-oriented code, instead of writing raw SQL queries.

**Create class inside todos/models.py**

**Create a PostgreSQL Database for Django**
psql --version OR brew list | grep postgresql
brew install postgresql
brew services start postgresql
psql postgres
CREATE DATABASE tododb;
CREATE USER myuser WITH PASSWORD 'pw';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tododb TO myuser;
\q

**Check DB is there**
psql postgres
\l
DROP DATABASE "petproject_db"; #if not needed
postgres, template0, and template1 are system databases and should not be deleted. They are needed by PostgreSQL for various internal operations.

**Check users**
postgres=# \du

**If encountering issues:**
sudo su
adduser postgres
usermod -aG sudo postgres
exit
sudo -u postgres psql OR psql -U postgres

**Add DB data in Settings**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tododb',
		'USER': 'myuser',
		'PASSWORD': 'pw',
		'HOST': 'localhost',
    }
}

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

**Configure routing for the app**