from django.db import models

# Create your models here.

class Printers(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=20)
    photo = models.ImageField()

class Cameras(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=20)

