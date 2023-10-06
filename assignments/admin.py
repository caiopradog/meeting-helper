from django.contrib import admin
from .models import Assignment, Event
# Register your models here.


@admin.register(Assignment)
class JobModelDataAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'assignee_name',
        'assignment'
    )
    list_filter = [
        'date',
        'assignee',
        'assignment'
    ]
    ordering = ['-date']

    def assignee_name(self, obj):
        return obj.assignee

    assignee_name.short_description = 'Voluntário'


admin.site.register(Event)
