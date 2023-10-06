from assignments.models import Assignment
from django import template
register = template.Library()


@register.filter
def get_assignment_full_name(value):
    return [choice[1] for choice in Assignment.ASSIGNMENT_CHOICES if choice[0] == value][0]


@register.filter
def get_assignement_abreviated_name(value):
    name = get_assignment_full_name(value)
    return name.replace('Indicador', 'Ind.').replace('Microfone', 'Mic.').replace('Estacionamento', 'Estac.')


@register.filter
def get_assignment_icon(value):
    if value == Assignment.MICROPHONE_LEFT or value == Assignment.MICROPHONE_RIGHT:
        return 'fa-solid fa-microphone'
    elif value == Assignment.READ_WATCHTOWER:
        return 'fa-solid fa-book-open'
    elif value == Assignment.PUBLIC_MEETING_CONDUCTOR:
        return 'ri-keynote-fill'
    elif value == Assignment.INDICATOR_ENTRANCE:
        return 'fa-solid fa-door-open'
    elif value == Assignment.INDICATOR_PARKING:
        return 'fa-solid fa-car-side'
    elif value == Assignment.INDICATOR_AUDITORIUM:
        return 'fa-solid fa-chair'
    elif value == Assignment.AUDIO_VIDEO:
        return 'fa-solid fa-computer'
    return ''
