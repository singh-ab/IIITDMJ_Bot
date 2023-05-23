from django.db import models

# Create your models here.
class Student (models.Model) :
    name=models.CharField(max_length=255 , primary_key=True)
    about = models.TextField(max_length=5000)
    def __str__(self):
        return self.name

# Create your models here.
class Places (models.Model) :
    name=models.CharField(max_length=255 , primary_key=True)
    about = models.TextField(max_length=5000)
    def __str__(self):
        return self.name
    