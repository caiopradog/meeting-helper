# Generated by Django 4.2.1 on 2023-05-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0006_alter_job_can_meeting_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='can_meeting_director',
        ),
        migrations.AddField(
            model_name='job',
            name='can_public_meeting_conductor',
            field=models.BooleanField(default=False, verbose_name='Public Meeting Conductor'),
        ),
    ]
