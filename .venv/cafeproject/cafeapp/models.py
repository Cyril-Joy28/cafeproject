from django.db import models
from django.db.models import CharField


class booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    seating = models.CharField(max_length=50)
    people = models.IntegerField()
    occasion = models.CharField(max_length=50)
    message = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"


class Staff(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=15)    
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    shift = models.CharField(max_length=10)


class up(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=20)


class login(models.Model):
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=10)