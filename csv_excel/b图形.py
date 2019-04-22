#!/usr/bin/python3
#coding:utf-8
from pyecharts import Bar
from csv_excel.a图形 import bar_tu
import os
import json

path = 'd:/data'

for root,dir,files in os.walk(path):
    # print(root,dir,files)
    for file in files:
        if file == 'mouth.txt':
            file_name = os.path.join(root,file)
            # print(root)
            # print(file_name)
            with open(file_name,'r',encoding='gb18030',newline='') as dict_file:
                fileread = dict_file.read()
                #json.loads 必须是双引号
                bar_tu(json.loads(fileread),'月',root)



# if __name__ == "__main__":
#     pass