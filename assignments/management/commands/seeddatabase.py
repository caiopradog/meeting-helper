from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Seed users and initial assignments"

    def handle(self, *args, **options):
        call_command('loaddata', 'fixtures/users.json')
        call_command('loaddata', 'fixtures/people.json')
        call_command('loaddata', 'fixtures/jobs.json')
        call_command('loaddata', 'fixtures/assignments.json')
        call_command('loaddata', 'fixtures/config.json')
        call_command('loaddata', 'fixtures/event.json')

        self.stdout.write(self.style.SUCCESS('Database was successfully seeded'))
