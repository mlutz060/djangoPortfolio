from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter proeject name')

    description = models.TextField(max_length=1000, help_text='Enter a description')

    link = models.CharField(max_length=500)
     
    def __str__(self):
        return self.name
    
