#!/usr/bin/python3
#coding:utf-8
from collections import Counter
import xlrd

outfile1 = 'C:/Users/DC_JL/Desktop/fb/贷记卡.txt'
file_name1 = 'C:/Users/DC_JL/Desktop/fb/贷记卡.xlsx'
workbook1 = xlrd.open_workbook(file_name1)
sheet1 = workbook1.sheet_by_index(0)
cols1 = sheet1.col_values(0)
count_name = Counter(cols1)
with open(outfile1,'w',encoding='gb18030',newline='') as f:
    for key,value in count_name.items():
        f.write('{0:s},{1:d}\n'.format(key,value))




if __name__ == "__main__":
    pass