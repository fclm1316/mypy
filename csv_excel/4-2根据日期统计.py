#!/usr/bin/python3
# coding:utf-8
import sys
import pandas as pd
from collections import Counter
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
# 读取文件
data_frame = pd.read_csv(input_file, encoding='gb18030', low_memory=False)
# 读取workdate表格列值
workdate = data_frame.WORKDATE
# new_workdate = workdate.drop_duplicates()
# print(new_workdate)
list_workdate = []
# 组成一个列
for list_workdates in workdate:
    list_workdate.append(str(list_workdates))
# 对列中的元素统计
count_workdate = Counter(list_workdate)
# print(count_workdate)
with open(output_file, 'w', newline='') as  csv_out_file:
    filewriter = csv.writer(csv_out_file)
    # 排序
    for key, value in sorted(count_workdate.items()):
        key_value = [key, value]
        # print(key,value)
        filewriter.writerow(key_value)
