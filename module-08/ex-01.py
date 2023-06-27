from datetime import datetime


def get_days_from_today(date):
    now = datetime.now().date()
    date = date.split('-')
    delta = now - datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])).date()
    return delta.days


get_days_from_today('2020-10-09')
