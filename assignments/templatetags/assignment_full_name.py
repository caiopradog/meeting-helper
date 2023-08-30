from assignments.models import Assignment
from django import template
register = template.Library()


@register.filter
def get_assignment_full_name(value):
    return [choice[1] for choice in Assignment.ASSIGNMENT_CHOICES if choice[0] == value][0]


@register.filter
def get_assignement_abreviated_name(value):
    name = get_assignment_full_name(value)
    return name.replace('Indicador', 'Ind.').replace('Microfone', 'Mic.')
