from cgitb import text
from http import client
from turtle import title
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)


class Record(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE)
    direction = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    data = models.DateField()
    time = models.TimeField()


class Service(models.Model):
    provider = models.ForeignKey(Record, on_delete = models.CASCADE)
    doctor = models.CharField(max_length=50)
    text = models.TextField()
    
  
class Feedback(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    time_create = models.DateField()
    time_update = models.DateField()
    provider = models.ForeignKey(Service, on_delete = models.CASCADE)
