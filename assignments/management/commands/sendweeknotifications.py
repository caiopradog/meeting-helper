from django.core.management.base import BaseCommand
from assignments.models import Assignment
from datetime import date
from django.template.defaultfilters import date as format_date
from notifications.service import send_user_notification
import utils


class Command(BaseCommand):
    help = "Send week's assignment notifications"

    def add_arguments(self, parser):
        parser.add_argument('--date', help='Date to send')

    def handle(self, *args, **options):
        base_date = options.get('date')
        if base_date is None:
            base_date = date.today()
        else:
            base_date = date.fromisoformat(base_date)
        monday = utils.go_to_last_weekday(base_date, 'Monday', True)
        sunday = utils.go_to_next_weekday(monday, 'Sunday')

        assignments = Assignment.objects.filter(date__range=[monday, sunday]).filter(assignee=1)
        for assignment in assignments.only('assignee').distinct():
            assignee = assignment.assignee
            user_assignments = assignments.filter(assignee=assignee)
            head = f'Você tem {len(user_assignments)} {"designação" if len(user_assignments) == 1 else "designações"} essa semana!'
            body = '\n'.join(
                [f'{format_date(assignment.date, "d/m/Y")}: {assignment.get_assignment_display()}' for assignment in
                 user_assignments])
            payload = {
                'head': head,
                'body': body,
                "url": "https://caiopradog.com.br/designacoes"
            }
            send_user_notification(user=assignee.user, payload=payload, ttl=1000)

        self.stdout.write(self.style.SUCCESS('Sent notification'))
