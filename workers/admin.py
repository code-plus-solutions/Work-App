from django.contrib import admin

from .models import Worker


# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['pk','avatar', 'name', 'lastName', 'password', 'phone', 'address', 'city', 'state']
