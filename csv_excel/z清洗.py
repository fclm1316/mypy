#!/usr/bin/python3
#coding:utf-8
import csv
import pandas as pd
import os
import re

file_path ='d:/data/'

for root,dir,files in os.walk(file_path):
    for file in files:
        file_name = os.path.join(root,file)
        files = os.path.basename(file_name).split('.')
        out_file = os.path.join(root +'/' + str(files[0]) + '_new' + '.vsc')
        # print(out_file)
        if str(files[1]) == 'csv':
            print(file_name)
            with open(file_name,'r',encoding='gb18030',newline='') as read_file:
                with open(out_file,'w',encoding='gb18030',newline='') as write_file:
                    filereader = csv.reader(read_file)
                    filewrite = csv.writer(write_file)
                    for new_csv in filereader:
                        # print(new_csv)
                        if str(new_csv[43]) == '0000':
                            filewrite.writerow(new_csv)


# if __name__ == "__main__":
#     pass