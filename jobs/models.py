import datetime
from django.db import models

# Create your models here.
class Job(models.Model):
    #Properties
    image = models.ImageField(upload_to='images/')
    JobTitle = models.CharField(max_length=250,)
    Employeer = models.CharField(max_length=250,)
    StartDate = models.DateField(default=datetime.date.today)
    current = models.BooleanField(default=False)
    EndDate = models.DateField(default=datetime.date.today)
    Location = models.CharField(max_length=200,)
    Description = models.TextField(max_length=20000,)
    Relavance = models.BooleanField(default=True)

    def __str__(self):
        return self.JobTitle
    
    class Meta:
        ordering = ['-Relavance', '-EndDate']
    
class Project(models.Model):
    image = models.ImageField(upload_to='images/',default=' ')
    name = models.CharField(max_length=100, default=' ') 
    file = models.FileField()
    description = models.TextField(max_length=2000, default=' ')

    def __str__(self):
        return self.name
    
class Education(models.Model):
    image = models.ImageField(upload_to='images/',default=' ')
    nameOfSchool = models.CharField(max_length=100, default=' ')
    major = models.CharField(max_length= 150,default=' ') 
    degree = models.CharField(max_length= 150,default=' ') 
    StartDate = models.DateField(default=datetime.date.today)
    EndDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.major
    
    class Meta:
        ordering = ['-EndDate']