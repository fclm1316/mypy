#!/usr/bin/python3
#coding:utf-8
import sys
import os
import glob
from difflib import *
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: file :%s not found" % filename)
        sys.exit(1)
input_path1 = sys.argv[1]
input_path2 = sys.argv[2]
#定义一个空列表
diff_file_list =[]
#查找文件
for file_all_1 in glob.glob(os.path.join(input_path1,"*")):
    #获得文件名
    file_all_name = os.path.basename(file_all_1)
    #print(file_all_name)
    #在tmp2 目录中查找匹配文件是否存在
    if os.path.exists(input_path2 + '/' + file_all_name ):
        #在目录1 中打开文件
        file1_content = read_file(file_all_1)
        #在目录文件中打开文件
        file2_content = read_file(input_path2 + '/' + file_all_name )
        #print(file1_content)
        #print(file2_content)
        #difflib 比对文件
        d = HtmlDiff.make_file(HtmlDiff(),file1_content,file2_content)
        #定义产生报告的文件
        diff_file_html = os.path.join(file_all_name + '.html')
        #写入文件
        with open(diff_file_html,'w') as f :
            f.writelines(d)
    #不存在，加入空列表中
    else:
        diff_file_list.append(file_all_name)
print(diff_file_list)
