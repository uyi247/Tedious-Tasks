from django.db import models

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=100)
    time = models.IntegerField()
    person = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description 