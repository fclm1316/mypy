#!/usr/bin/python3
# coding:utf-8
import sys
import csv
import re

input_file = sys.argv[1]
output_file = sys.argv[2]
# errors=‘ignore’,使用更广阔的编码读取汉字，或者忽略
# with open(input_file,'r',encoding='gb18030',newline='') as filereader:
#     for row in filereader:
#         row = row.strip()
#         row_list = row.split(';')
#         #print(row_list)
#         patten = re.compile(',')
#         for eachone in row_list:
#             if patten.search(eachone):
#                 print(row_list,eachone)
# 打开文件
with open(input_file, 'r', encoding='gb18030', newline='') as csv_in_file:
    with open(output_file, 'w', encoding='gb18030', newline='') as csv_out_file:
        # 使用分隔符号
        filereader = csv.reader(csv_in_file, delimiter='\'')
        filewriter = csv.writer(csv_out_file)
        # 读取标题头
        header = next(filereader)
        # print(header)
        filewriter.writerow(header)
        for row_list in filereader:
            # 查找字符串里的逗号
            patten = re.compile(r',')
            # 创建新的列
            new_list = []
            for eachone in row_list:
                eachone_strip = eachone.strip()
                if eachone_strip:
                    if patten.search(eachone_strip):
                        # 替换逗号
                        replace = str(eachone_strip).replace(',', '-')
                        new_list.append(replace)
                    else:
                        new_list.append(eachone_strip)
                else:
                    eachone_strip = 'NULL'
                    new_list.append(eachone_strip)
            # filewriter.writerow(','.join(map(str,new_list))+'\n')
            filewriter.writerow(new_list)
