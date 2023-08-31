from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Assignment
from .service import get_period_meetings, generate_meeting_assignments, get_next_meeting_day
from utils import get_first_and_last_days_of_month
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from designacoes import renderers


@login_required(login_url='assignments.login')
def index(request):
    is_pdf = 'pdf' in request.GET
    month = int(request.GET.get('month', 0))
    base_date = datetime.now() + relativedelta(months=month)
    period_start, period_end = get_first_and_last_days_of_month(base_date=base_date)
    show_assignments = [
        Assignment.MICROPHONE_LEFT,
        Assignment.MICROPHONE_RIGHT,
        Assignment.AUDIO_VIDEO,
        Assignment.INDICATOR_PARKING,
        Assignment.INDICATOR_ENTRANCE,
        Assignment.INDICATOR_AUDITORIUM,
        Assignment.READ_WATCHTOWER,
        Assignment.PUBLIC_MEETING_CONDUCTOR
    ]
    meetings = get_period_meetings(
        period_start,
        period_end,
        show_assignments
    )
    next_meeting = get_next_meeting_day(date.today(), allow_same_day=True)

    pdf_url = request.get_full_path()
    if '?' in pdf_url:
        pdf_url = f'{pdf_url}&pdf'
    else:
        pdf_url = f'{pdf_url}?pdf'

    data = {
        'meetings': meetings,
        'next_meeting': next_meeting,
        'month': month,
        'base_date': base_date,
        'pdf_url': pdf_url
    }
    if is_pdf:
        weekend_meetings = [meeting for meeting in meetings if meeting['date'].weekday() >= 5]
        pdf_data = {
            **data,
            'weekend_meetings': weekend_meetings,
        }
        return renderers.render_to_pdf('pdf/midweek.html', pdf_data)
    return render(request, 'assignments/index.html', data)


def logout_view(request):
    logout(request)
    return redirect('assignments.login')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('assignments')

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        error = None
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('assignments')

        return render(request, 'login.html', {'login_error': True})
