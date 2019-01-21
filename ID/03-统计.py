#!/usr/bin/python3
#coding:utf-8
import os
import glob
import csv
import time

input_path= "D:/2000Wnew/sheng"
input_file = glob.glob(os.path.join(input_path,'*.csv'))
output_path = "D:/2000Wnew/sheng/tongji/"

def count_num(csv_filename):
   sun_man = 0
   sun_woman = 0
   S90 = 0
   S80 = 0
   S70 = 0
   S60 = 0
   S50 = 0
   S40 = 0
   S30 = 0
   S20 = 0
   Sxx = 0
   with open(csv_filename,'r',encoding='gb18030',newline='') as csv_readfile:
       readfile = csv.reader(csv_readfile)
       for lines in readfile:
           if lines[-1] == '男':
               sun_man = sun_man + 1
           else:
               sun_woman = sun_woman + 1
           if int(lines[3]) >= 1990:
               S90 = S90 +1
           elif int(lines[3]) >= 1980 :
               S80 = S80 +1
           elif int(lines[3]) >= 1970:
               S70 = S70 +1
           elif int(lines[3]) >= 1960:
               S60 = S60 +1
           elif int(lines[3]) >= 1950:
               S50 = S50 +1
           elif int(lines[3]) >= 1940 :
               S40 = S40 +1
           elif int(lines[3]) >= 1930 :
               S40 = S30 +1
           elif int(lines[3]) >= 1920 :
               S40 = S20 +1
           else:
               Sxx = Sxx +1
               # print(lines[3])
   sum_human = sun_man + sun_woman
   head_name = (os.path.basename(csv_filename).split('.')[0])
   a = (head_name,sum_human,sun_man,sun_woman,S90,S80,S70,S60,S50,S40,S30,S20,Sxx)
   filename = ''.join(output_path + 'heji'+ '.csv')
   # print(filename)
   with open(filename,'a',encoding='gb18030',newline='') as csv_writefile:
       writefile = csv.writer(csv_writefile)
       writefile.writerow(a)




def main(filename):
    count_num(filename)

if __name__ == '__main__':
    for a in input_file:
        t_start = time.process_time()
        main(a)
        t_end = time.process_time()
        t1 = t_end - t_start
        print('{0:s}  耗时: {1:.2f} s'.format(a,t1))
