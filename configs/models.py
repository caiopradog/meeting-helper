from django.db import models

# Create your models here.


class Config(models.Model):
    config = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.config.replace('_', ' ').title()
