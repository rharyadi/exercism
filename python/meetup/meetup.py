import calendar
import datetime

def meetup_day(year, month, dayweek, th):
    cal = calendar.monthcalendar(year, month)
    dayweek = list(calendar.day_name).index(dayweek)
    if th == 'teenth':
        for i in cal:
            if i[dayweek] in range(13,19+1):
                date = i[dayweek]
    else:
        th_dict = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last':-1}
        th = th_dict[th]
        candidate = [i[dayweek] for i in cal if i[dayweek]]
        date = candidate[th]
    return datetime.date(year,month,date)
