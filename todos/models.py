from django.db import models

# Create your models here.
class Todo(models.Model):
    date = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    vin = models.CharField(max_length=200)