from .models import Person, Job
from assignments.models import Assignment
from django.db.models import Max, Q


def filter_volunteer_by_assignment(job_object, assignment):
    if (assignment == Assignment.INDICATOR_PARKING
            or assignment == Assignment.INDICATOR_AUDITORIUM
            or assignment == Assignment.INDICATOR_ENTRANCE):
        job_object = job_object.filter(can_indicator=True)
    elif assignment == Assignment.MICROPHONE_LEFT or assignment == Assignment.MICROPHONE_RIGHT:
        job_object = job_object.filter(can_microphone=True)
    elif assignment == Assignment.AUDIO_VIDEO:
        job_object = job_object.filter(can_sound=True)
    elif assignment == Assignment.FIELD_CONDUCTOR:
        job_object = job_object.filter(can_field_service_conductor=True)
    elif assignment == Assignment.PUBLIC_MEETING_CONDUCTOR:
        job_object = job_object.filter(can_public_meeting_conductor=True)
    elif assignment == Assignment.READ_WATCHTOWER:
        job_object = job_object.filter(can_read_watchtower=True)

    return job_object


def get_next_volunteer_for_assignment(assignment, working_people):
    current_assignment = Q(volunteer__assignment__assignment=assignment)
    people = Job.objects\
        .annotate(last_assignment=Max('volunteer__assignment__date', filter=current_assignment))\
        .order_by('last_assignment', 'volunteer__name')\
        .exclude(volunteer_id__in=working_people)
    people = filter_volunteer_by_assignment(people, assignment)

    return people[0].volunteer


def get_assignment_list_by_volunteer_number(exclude=[]):
    assignments = {}
    for (assignment, name) in Assignment.ASSIGNMENT_CHOICES:
        people = Job.objects
        people = filter_volunteer_by_assignment(people, assignment)
        assignments[assignment] = people.count()

    return list(filter(lambda choice: choice not in exclude, sorted(assignments)))
