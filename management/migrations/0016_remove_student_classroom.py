# Generated by Django 4.1.13 on 2024-01-02 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_delete_issue_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
    ]
