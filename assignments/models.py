from django.db import models
from django.contrib.auth.models import User
from volunteers.models import Person

# Create your models here.


class Assignment(models.Model):
    MICROPHONE_LEFT = 'ML'
    MICROPHONE_RIGHT = 'MR'
    INDICATOR_AUDITORIUM = 'IA'
    INDICATOR_ENTRANCE = 'IE'
    INDICATOR_PARKING = 'IP'
    AUDIO_VIDEO = 'AV'
    FIELD_CONDUCTOR = 'FC'
    READ_WATCHTOWER = 'RW'
    PUBLIC_MEETING_CONDUCTOR = 'MC'
    ASSIGNMENT_CHOICES = [
        (MICROPHONE_LEFT, 'Microfone Direito'),
        (MICROPHONE_RIGHT, 'Microfone Esquerdo'),
        (INDICATOR_AUDITORIUM, 'Indicador Auditório'),
        (INDICATOR_ENTRANCE, 'Indicador Entrada'),
        (INDICATOR_PARKING, 'Indicador Estacionamento'),
        (AUDIO_VIDEO, 'Áudio e Vídeo'),
        (FIELD_CONDUCTOR, 'Dirigente de Campo'),
        (READ_WATCHTOWER, 'Leitor de Sentinela'),
        (PUBLIC_MEETING_CONDUCTOR, 'Presidente'),
    ]

    date = models.DateField()
    assignee = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    assignment = models.CharField(
        max_length=2,
        choices=ASSIGNMENT_CHOICES
    )

    def __str__(self):
        return f'{self.date} - {self.get_assignment_display()} - {self.assignee}'


class Event(models.Model):
    OVERSEER = 1
    CONGRESS = 2
    ASSEMBLY = 3
    MEMORIAL = 4
    EXCEPTION_TYPES = [
        (OVERSEER, 'Visita do Superintendente'),
        (CONGRESS, 'Congresso'),
        (ASSEMBLY, 'Assembleia'),
        (MEMORIAL, 'Celebração')
    ]
    type = models.IntegerField(choices=EXCEPTION_TYPES)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'{self.get_type_display()}'
