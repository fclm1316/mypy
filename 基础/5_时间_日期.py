#!/usr/bin/env python3
from datetime import date,time,datetime,timedelta
today = date.today()
print('打印时间格式时间 {0!s}'.format(today))
print('打印时间格式年 {0:d}'.format(today.year))
print('打印时间格式月 {0:d}'.format(today.month))
print('打印时间格式日 {0:d}'.format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))
print("Output #45-1: {0!s}".format(current_datetime.year))
print("Output #45-2: {0!s}".format(current_datetime.month))
print("Output #45-3: {0!s}".format(current_datetime.day))
print("Output #45-4: {0!s}".format(current_datetime.hour))
print("Output #45-5: {0!s}".format(current_datetime.minute))
print("Output #45-6: {0!s}".format(current_datetime.second))
print("Output #45-7: {0!s}".format(current_datetime.microsecond))
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days,eight_hours.seconds))
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))
#字符串输出时间
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
print("Output #56: {!s}".format(datetime.date(datetime.strptime \
                                                  (date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime \
                                                  (date4, '%B %d, %Y'))))
