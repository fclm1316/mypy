#!/usr/bin/env python3
import sys
import os
import glob
input_path = sys.argv[1]
all_file_path = glob.glob(os.path.join(input_path,'*.txt'))
print('查找的txt文件有：')
print(all_file_path)
print()
#print('使用字符串查找 str.find 结尾sh')
all_file_path2 = glob.glob(os.path.join(input_path,'*.*'))
for names in all_file_path2:
    all_names= os.path.basename(names)
    #print(all_names)
    ss = all_names.find('.sh')
    if ss > 0:
        print(all_names)
        print(ss)
#没办法过滤
