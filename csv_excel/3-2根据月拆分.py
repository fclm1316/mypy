# ！/usr/bin/python3
# coding:utf-8

import sys
from datetime import datetime
import pandas as pd
import csv
import os

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file, encoding='gb18030', low_memory=False)
workdate = data_frame.WORKDATE
list_workdate_mouth = []
for workdate_mouth in workdate:
    list_workdate_mouth.append(str(workdate_mouth))
mouth_list = []
for aa in list_workdate_mouth:
    bb = datetime.strptime(aa, '%Y%m%d')
    cc = bb.strftime('%Y%m')
    mouth_list.append(cc)
mouth_list = sorted(set(mouth_list))
# print(mouth_list)
with open(input_file, 'r', encoding='gb18030', newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file, delimiter=',')
    # 读取标题头
    header = next(filereader)
    # 根据年份创建新文件
    for output_mouth in mouth_list:
        output_file_mouth = os.path.join(output_file + '_' + output_mouth + '.csv')
        with open(output_file_mouth, 'w', encoding='gb18030', newline='') as csv_out_file:
            filewriter = csv.writer(csv_out_file)
            # 写入头
            filewriter.writerow(header)
    for BB in filereader:
        # 文件中获得日期,格式化日期
        work_list = BB[0]
        work_date = datetime.strptime(work_list, '%Y%m%d')
        work_mouth = work_date.strftime('%Y%m')
        # 打开对应的年份的文件
        output_file_mouth = os.path.join(output_file + '_' + work_mouth + '.csv')
        with open(output_file_mouth, 'a+', encoding='gb18030', newline='') as csv_out_file:
            filewriter = csv.writer(csv_out_file)
            for AA in mouth_list:
                # 匹配写入文件
                if AA == work_mouth:
                    filewriter.writerow(BB)
