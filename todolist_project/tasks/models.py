from django.db import models

# Create your models here.

####### NEW #######
# defines a new model called Task. It inherits from models.Model, making it a Django model.
class Task(models.Model):
	# CharField, which represents a short text field in the database. 
	# max_length=200 means the maximum length of the text is 200 characters.
    title = models.CharField(max_length=200)
	# BooleanField, which stores True or False. default=False sets the default value to False.
    completed = models.BooleanField(default=False)

	# __str__ method, which returns a string representation of the model.
    def __str__(self):
        return self.title
####### NEW #######

# Models are a fundamental part of the framework's data management system. 
# They define the structure of your db tables and provide a way to interact 
# with your data using Python. 
# 
# A model maps to a single database table, 
# each model class corresponds to a table in your database.