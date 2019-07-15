#!/usr/bin/python3
#coding:utf-8
from collections import Counter
import xlrd
outfile1 = 'C:/Users/DC_JL/Desktop/fb/一码通1.txt'
file_name1 = 'C:/Users/DC_JL/Desktop/fb/一码通.xlsx'
workbook1 = xlrd.open_workbook(file_name1)
sheet1 = workbook1.sheet_by_index(0)
cols1 = sheet1.col_values(0)
count_name = Counter(cols1)
print(count_name)
with open(outfile1,'w',encoding='gb18030',newline='') as f:
    for key,value in count_name.items():
        f.write('{0:s},{1:d}\n'.format(key,value))


outfile2 = 'C:/Users/DC_JL/Desktop/fb/一码通2.txt'
file_name2 = 'C:/Users/DC_JL/Desktop/fb/2018年度一码通有效户新增奖励.xlsx'
workbook2 = xlrd.open_workbook(file_name2)
sheet2 = workbook2.sheet_by_index(0)
with open(outfile2,'w',encoding='gb18030',newline='') as f:
    for i in range(2,355):
        s2_key = sheet2.cell_value(i,1)
        s2_value = sheet2.cell_value(i,3)
        f.write('{0:s},{1:.0f}\n'.format(s2_key,s2_value))
#



if __name__ == "__main__":
    pass