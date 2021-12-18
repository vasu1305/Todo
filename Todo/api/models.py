from django.db import models
from django.db.models.fields import *

# Create your models here.

class Todo(models.Model):
    tasks = models.CharField(max_length=115)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasks
    
    class Meta:
        ordering = ['-created']
