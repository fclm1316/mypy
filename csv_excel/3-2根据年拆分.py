#!/usr/bin/python3
#coding:utf-8
import sys
import os
import csv
from datetime import datetime
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file,encoding='gb18030',low_memory=False)
#读取workdate表格列值
workdate = data_frame.WORKDATE
list_workdate = []
#组成一个列
for list_workdates in workdate:
    list_workdate.append(str(list_workdates))
year_list =[]
for aa in list_workdate:
    bb = datetime.strptime(aa,'%Y%m%d')
    cc = bb.strftime('%Y')
    year_list.append(cc)
year_list = sorted(set(year_list))
print(year_list)
#读取文件
with open(input_file,'r',encoding='gb18030',newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file,delimiter=',')
        #读取标题头
    header = next(filereader)
    for output_year in year_list:
        output_file_year = os.path.join(output_file+'_'+output_year+'.csv')
        with open(output_file_year,'w',encoding='gb18030',newline='') as csv_out_file:
            filewriter = csv.writer(csv_out_file)
            filewriter.writerow(header)
    for BB in filereader:
        work_list = BB[0]
        work_date = datetime.strptime(work_list,'%Y%m%d')
        work_year = work_date.strftime('%Y')
        output_file_year = os.path.join(output_file+'_'+work_year+'.csv')
        with open(output_file_year,'a+',encoding='gb18030',newline='') as csv_out_file:
            filewriter = csv.writer(csv_out_file)
            for AA in year_list:
                #filewriter.writerow(header)
                if  AA == work_year:
                    filewriter.writerow(BB)

