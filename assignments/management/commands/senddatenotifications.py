from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from assignments.models import Assignment
from datetime import date
from notifications.service import send_user_notification


class Command(BaseCommand):
    help = "Send date's assignment notifications"

    def add_arguments(self, parser):
        parser.add_argument('--date', help='Date to send')

    def handle(self, *args, **options):
        base_date = options.get('date')
        if base_date is None:
            base_date = date.today()
        else:
            base_date = date.fromisoformat(base_date)

        assignments = Assignment.objects.filter(date=base_date)

        for assignment in assignments:
            payload = {
                'head': 'Você tem uma designação hoje!',
                'body': assignment.get_assignment_display()
            }
            send_user_notification(user=assignment.assignee.user, payload=payload, ttl=1000)

        self.stdout.write(self.style.SUCCESS('Sent notification'))
