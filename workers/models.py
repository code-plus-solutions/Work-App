from django.db import models

from works.models import Work


# Create your models here.
class Worker(models.Model):
    avatar = models.ImageField(upload_to="media", blank=True, null=True)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    work = models.ManyToManyField(Work, related_name="Worker")

    def __str__(self):
        return f"{self.pk}_{self.name}{self.lastName}"
