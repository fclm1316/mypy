#!/usr/bin/python3
#coding:utf-8
from collections import Counter
import xlrd

file1 = 'C:/Users/DC_JL/Desktop/fb/ETC11-12月.xlsx'
outfile1 = 'C:/Users/DC_JL/Desktop/fb/ETC1.txt'
workbook1 = xlrd.open_workbook(file1)
sheet1 = workbook1.sheet_by_index(0)
cols1 = sheet1.col_values(0)
count_name = Counter(cols1)
# print(count_name)
with open(outfile1,'w',encoding='gb18030',newline='') as f:
    for key,value in count_name.items():
        f.write('{0:s},{1:d}\n'.format(key,value))


file2 = 'C:/Users/DC_JL/Desktop/fb/2018年11月12月ETC营销奖励.xlsx'
outfile2 = 'C:/Users/DC_JL/Desktop/fb/ETC2.txt'
workbook2 = xlrd.open_workbook(file2)
sheet2 = workbook2.sheet_by_index(0)
with open(outfile2,'w',encoding='gb18030',newline='') as f:
    nrows = sheet2.nrows
    for i in range(nrows):
        s2_key = str(sheet2.cell_value(i,1))
        s2_value = sheet2.cell_value(i,3)
        if sheet2.cell_type(i,3) == 2:
            f.write('{0:s},{1:.0f}\n'.format(s2_key,s2_value))
            # print(s2_value)





if __name__ == "__main__":
    pass