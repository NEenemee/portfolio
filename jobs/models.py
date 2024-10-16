from django.db import models

# Create your models here.
class Job(models.Model):
    #Properties
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
