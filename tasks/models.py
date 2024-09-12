from django.db import models

# Create your models here.

# Declare a new model with the name "Task"
class Task(models.Model):
    # Fields of the model
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    # Renames the instances of the model with their title name
    def __str__(self):
        return self.title


# After creating this model, we need to run two commands in order to create Database for the same. 



# The __str__ method is a special method in Python that is called by the print function to get a string representation of an object.
# $ python manage.py shell
# >>> from tasks.models import Task
# >>> task = Task.objects.first()
# >>> print(task)
# # Output: "Example Task Title" (assuming the title of the task is "Example Task Title")
