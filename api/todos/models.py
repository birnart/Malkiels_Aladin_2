from django.db import models

#python manage.py runserver

# Create your models here.

#replace function with the imported algrotihms and use the variables here  

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        """A string representation of the model."""
        return self.title
 