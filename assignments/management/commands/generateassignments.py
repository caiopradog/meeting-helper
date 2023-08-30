from django.core.management.base import BaseCommand, CommandError
from dateutil.relativedelta import relativedelta
from assignments.models import Assignment
from assignments.service import generate_meeting_assignments
from datetime import date
from utils import get_first_and_last_days_of_month


class Command(BaseCommand):
    help = "Generate next month's assignment"

    def add_arguments(self, parser):
        parser.add_argument('--date', help='Date to generate')

    def handle(self, *args, **options):
        base_date = options.get('date')
        if base_date is None:
            last_assignment_date = Assignment.objects.order_by('-date')[0].date
            base_date = last_assignment_date + relativedelta(months=1)
        else:
            base_date = date.fromisoformat(base_date)

        period_start, period_end = get_first_and_last_days_of_month(base_date=base_date)
        generate_meeting_assignments(period_start, period_end, delete_assignments=True)

        self.stdout.write(self.style.SUCCESS('Generated assignments'))
