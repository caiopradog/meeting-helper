# Generated by Django 4.2.1 on 2023-08-01 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0013_remove_duplicate_name_columns'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]
