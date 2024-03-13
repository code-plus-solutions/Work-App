from django.db import models


# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=100)

