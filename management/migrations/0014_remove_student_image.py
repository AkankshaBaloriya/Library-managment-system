# Generated by Django 4.1.13 on 2024-01-01 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_issuedbook_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]