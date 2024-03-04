"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    date_today = datetime.now()
    print(date_today)
    delta = timedelta(days=1)
    date_yesterday = date_today - delta
    print(date_yesterday)
    delta_month = timedelta(days=30)
    date_30_days_ago = date_today - delta_month
    print(date_30_days_ago)


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(type(date_dt))
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
