from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def user_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.user_name()

    class Meta:
        verbose_name_plural = 'people'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.person.save()


class Job(models.Model):
    volunteer = models.OneToOneField(Person, on_delete=models.DO_NOTHING)
    can_microphone = models.BooleanField(default=False, verbose_name='Microphone')
    can_indicator = models.BooleanField(default=False, verbose_name='Indicator')
    can_sound = models.BooleanField(default=False, verbose_name='Sound')
    can_field_service_conductor = models.BooleanField(default=False, verbose_name='Field Service Conductor')
    can_read_watchtower = models.BooleanField(default=False, verbose_name='Watchtower Reader')
    can_public_meeting_conductor = models.BooleanField(default=False, verbose_name='Public Meeting Conductor')

    def get_list_of_jobs(self):
        jobs = {
            'Microfone': self.can_microphone,
            'Indicator': self.can_indicator,
            'Áudio e Vídeo': self.can_sound,
            'Dirigente de Campo': self.can_field_service_conductor,
            'Leitor da Sentinela': self.can_read_watchtower,
            'Presidente': self.can_public_meeting_conductor
        }
        return jobs

    def get_list_of_allowed_jobs(self):
        jobs = self.get_list_of_jobs()
        filtered_jobs = list(filter(lambda job: job[1], jobs.items()))
        return [job[0] for job in filtered_jobs]

    def __str__(self):
        return f"Designações do {self.volunteer}"
