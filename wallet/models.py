from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=0)
