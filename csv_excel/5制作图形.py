#!/usr/bin/python3
#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import csv
import sys
input_file = sys.argv[1]
workdate = []
t_sum = []
with open(input_file,'r',newline='') as csv_in_put:
    plots = csv.reader(csv_in_put,delimiter=',')
    for row in plots:
        workdate.append(str(row[0]))
        t_sum.append(int(row[1]))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(workdate,t_sum)
ax1.set_xticks(workdate)
plt.xlabel('mouth')
plt.ylabel('sum')
plt.title('aa')
plt.xticks(rotation=45)
#plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
