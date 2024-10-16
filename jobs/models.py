import datetime
from django.db import models

# Create your models here.
class Job(models.Model):
    #Properties
    image = models.ImageField(upload_to='images/')
    JobTitle = models.CharField(max_length=250,)
    Employeer = models.CharField(max_length=250,)
    StartDate = models.DateField(default=datetime.date.today)
    EndDate = models.DateField(default=datetime.date.today)
    Location = models.CharField(max_length=200,)
    Description = models.TextField(max_length=20000,)
