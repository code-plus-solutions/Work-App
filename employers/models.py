from django.db import models


# Create your models here.
class Employer(models.Model):
    avatar = models.ImageField(upload_to="media")
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}_{self.name}{self.lastName}"
