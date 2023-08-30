from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


def translate_weekday(weekday):
    days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    return days[weekday]


def go_to_next_weekday(base_date, day):
    weekday = translate_weekday(day)
    days = (weekday - base_date.weekday() - 1) % 7 + 1

    return base_date + timedelta(days=days)


def get_first_and_last_days_of_month(base_date=datetime.now(), add_months=0):
    first_day = get_first_day_of_month(base_date)
    end_month = base_date + relativedelta(months=add_months)
    last_day = get_last_day_of_month(end_month)
    return first_day, last_day


def get_first_day_of_month(base_date):
    return base_date.replace(day=1)


def get_last_day_of_month(base_date):
    next_month = base_date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)
