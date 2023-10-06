from django.contrib import admin
from .models import Person, Job

# Register your models here.


@admin.register(Person)
class VolunteerModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


@admin.register(Job)
class JobModelDataAdmin(admin.ModelAdmin):
    list_display = (
        'volunteer',
        'can_microphone',
        'can_indicator',
        'can_sound',
        'can_field_service_conductor',
        'can_read_watchtower',
        'can_public_meeting_conductor'
    )
    list_filter = [
        'can_microphone',
        'can_indicator',
        'can_sound',
        'can_field_service_conductor',
        'can_read_watchtower',
        'can_public_meeting_conductor'
    ]
    ordering = ['volunteer']

    def volunteer_name(self, obj):
        return obj.volunteer.name

    volunteer_name.short_description = 'Pessoa'
