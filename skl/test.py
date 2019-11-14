#encoding:utf-8
import time
from datetime import date
time_date = date.today().strftime('%Y%m%d')
time_time = time.strftime('%H%M%S')
xzb = ''.join(time_date+time_time)
time_now = int(time.time())
print(time_now)
