#!/usr/bin/python3
#coding:utf-8
from collections import Counter
import xlrd

file1 = 'C:/Users/DC_JL/Desktop/fb/电子账户11月.xlsx'
file2 = 'C:/Users/DC_JL/Desktop/fb/电子账户12月.xlsx'
outfile1 = 'C:/Users/DC_JL/Desktop/fb/电子账户.txt'

def dszh(name):
    workbook1 = xlrd.open_workbook(name)
    sheet1 = workbook1.sheet_by_index(0)
    cols1 = sheet1.col_values(1)
    count_name = Counter(cols1)
    return count_name

dict1 = dszh(file1)
dict2 = dszh(file2)

dict3 = dict1 + dict2
with open(outfile1,'w',encoding='gb18030',newline='') as f:
    for key,value in dict3.items():
        f.write('{0:s},{1:d}\n'.format(key,value))

if __name__ == "__main__":
    pass