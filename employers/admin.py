from django.contrib import admin
from .models import Employer


# Register your models here.
@admin.register(Employer)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'avatar', 'name', 'lastName', 'password', 'phone', 'address', 'city', 'state']
