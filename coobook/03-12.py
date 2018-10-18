#!/usr/bin/python3
#coding:utf-8
#时间转换
from datetime import timedelta ,datetime
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)
print(c.days)
print(c.seconds / 3600 )
print(c.total_seconds())
d = datetime(2018,10,10)
print(d+timedelta(days=10))
e = datetime(2013,10,26)
f = d - e
print(f.days)
now = datetime.today()
print(now + timedelta(minutes=10))
