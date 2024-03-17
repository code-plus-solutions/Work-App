from django.contrib import admin
from .models import Sms


# Register your models here.

@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'code']
