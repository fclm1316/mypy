#!/usr/bin/python3
# coding:utf-8
import json
import os
from collections import Counter
from csv_excel.a图形 import bar_tu

path = 'd:/data'

dict_mouth = {}
for root, dir, files in os.walk(path):
    # print(root,dir,files)
    for file in files:
        if file == 'mouth.txt':
            file_name = os.path.join(root, file)
            # print(root)
            # print(file_name)
            with open(file_name, 'r', encoding='gb18030', newline='') as dict_file:
                file_json = json.loads(dict_file.read())
                # 字典合计 累加 相加
                dict_mouth = dict(Counter(dict_mouth) + Counter(file_json))

# print(dict_mouth)
bar_tu(dict_mouth, '年月', 'd:/data/')

# if __name__ == "__main__":
#     pass
