# Generated by Django 4.2.1 on 2023-05-06 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0010_alter_job_volunteer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Volunteer',
            new_name='Person',
        ),
    ]
