#!/usr/bin/python3
#coding:utf-8
import sys
import csv
import re
input_file = sys.argv[1]
output_file = sys.argv[2]
#errors=‘ignore’,使用更广阔的编码读取汉字，或者忽略
# with open(input_file,'r',encoding='gb18030',newline='') as filereader:
#     for row in filereader:
#         row = row.strip()
#         row_list = row.split(';')
#         #print(row_list)
#         patten = re.compile(',')
#         for eachone in row_list:
#             if patten.search(eachone):
#                 print(row_list,eachone)
with open(input_file,'r',encoding='gb18030',newline='') as csv_in_file:
    with open(output_file,'w',encoding='gb18030',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=';')
        for row_list in filereader:
            patten = re.compile(',')
            new_list=[]
            for eachone in row_list:
                if patten.search(eachone):
                    replace = str(eachone).replace(',','-')
                    new_list.append(replace)
                else:
                    new_list.append(eachone)
            csv_out_file.write(','.join(map(str,new_list))+'\n')

