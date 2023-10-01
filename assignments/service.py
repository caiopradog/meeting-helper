from .models import Assignment, Event
from volunteers.service import get_next_volunteer_for_assignment, get_assignment_list_by_volunteer_number
from configs.models import Config
import utils


def get_period_meetings(period_start, period_end, assignment_filter=None):
    assignments = get_period_assignments(period_start, period_end, assignment_filter)
    assignments.order_by('assignment')
    meetings = get_meeting_days(period_start, period_end)

    for meeting in meetings:
        meeting_assignments = assignments.filter(date=meeting['date']).order_by('assignment')
        meeting['assignments'] = {assignment.assignment: assignment.assignee for assignment in meeting_assignments}

    return [meeting for meeting in meetings if len(list(meeting['assignments'])) > 0 or meeting['event'] is not None]


def generate_meeting_assignments(period_start, period_end, delete_assignments=False):
    meetings = get_meeting_days(period_start, period_end)
    period_assignments = get_period_assignments(period_start, period_end)
    if delete_assignments:
        period_assignments.delete()

    for meeting in meetings:
        new_assignments = []
        for assignment, value in meeting['assignments'].items():
            has_assignment = period_assignments.filter(date=meeting['date'], assignment=assignment).exists()
            if delete_assignments or not has_assignment:
                assigned = [volunteer.id for volunteer in meeting['assignments'].values() if volunteer is not None]
                volunteer = get_next_volunteer_for_assignment(assignment, assigned)
                meeting['assignments'][assignment] = volunteer
                new_assignments.append(Assignment(assignee=volunteer, assignment=assignment, date=meeting['date']))
        Assignment.objects.bulk_create(new_assignments)

    return meetings


def get_period_assignments(period_start, period_end, assignment_filter=None):
    assignments = Assignment.objects\
        .filter(date__gte=period_start)\
        .filter(date__lte=period_end)
    if assignment_filter:
        assignments = assignments.filter(assignment__in=assignment_filter)

    return assignments


def get_next_meeting_day(date, allow_same_day=False):
    configs = Config.objects.filter(config__endswith='meeting')
    next_meeting = None
    for config in configs:
        next_day = utils.go_to_next_weekday(date, config.value, allow_same_day)
        if not next_meeting or next_meeting > next_day:
            next_meeting = next_day

    return next_meeting


def get_meeting_days(period_start, period_end):
    days = []
    date = get_next_meeting_day(period_start, True)
    while date <= period_end:
        period_event = Event.objects.filter(date_start__lte=date).filter(date_end__gte=date).first()
        assignments_filter = [Assignment.FIELD_CONDUCTOR]
        if period_event:
            event_name = period_event.get_type_display()
            if period_event.type == Event.ASSEMBLY or period_event.type == Event.CONGRESS:
                assignments_filter = [choice[0] for choice in Assignment.ASSIGNMENT_CHOICES]
            elif period_event.type == Event.OVERSEER:
                assignments_filter.append(Assignment.READ_WATCHTOWER)
        if date.weekday() < 5:
            assignments_filter.append(Assignment.PUBLIC_MEETING_CONDUCTOR)
            assignments_filter.append(Assignment.READ_WATCHTOWER)

        meeting_assignments = get_assignment_list_by_volunteer_number(assignments_filter)
        days.append({
            'date': date,
            'assignments': {assignment: None for assignment in meeting_assignments},
            'event': period_event,
        })
        date = get_next_meeting_day(date)

    return days
