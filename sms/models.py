from django.db import models


# Create your models here.

class Sms(models.Model):
    phone = models.CharField(max_length=12)
    code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.pk}{self.phone}_{self.code}"
