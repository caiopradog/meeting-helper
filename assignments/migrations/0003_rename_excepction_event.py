# Generated by Django 4.2.1 on 2023-05-12 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_excepction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Excepction',
            new_name='Event',
        ),
    ]
