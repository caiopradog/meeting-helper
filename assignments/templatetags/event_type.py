from assignments.models import Event

from django import template
register = template.Library()


@register.filter
def event_type(value):
    if value == 'OVERSEER':
        return Event.OVERSEER
    if value == 'CONGRESS':
        return Event.CONGRESS
    if value == 'ASSEMBLY':
        return Event.ASSEMBLY
    if value == 'MEMORIAL':
        return Event.MEMORIAL
    return ''
