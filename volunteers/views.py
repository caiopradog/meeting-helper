from django.http import HttpResponse
from .models import Person, Job

# Create your views here.


def index(request):
    volunteers = Person.objects.all()
    volunteers_names = [volunteer.name() for volunteer in volunteers]
    return HttpResponse(f"""Hello, world! We're at the volunteers index.<br>
    These are the names of the volunteers:<br>
    {'<br>'.join(volunteers_names)}""")
