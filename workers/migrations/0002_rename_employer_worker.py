# Generated by Django 5.0.3 on 2024-03-13 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employer',
            new_name='Worker',
        ),
    ]
