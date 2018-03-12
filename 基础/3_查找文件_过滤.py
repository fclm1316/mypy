#!/usr/bin/env python3
import sys
import os
import glob
import re
input_path = sys.argv[1]
all_file_path = glob.glob(os.path.join(input_path,'*.txt'))
print('所有文件1：')
all_files = os.listdir(input_path)
print('所有文件2：')
print(all_files)
print('++++++++++++++++++++++++++++++++++++++++++++')
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
# topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。
# 如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
# onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
# followlinks -- 设置为 true，则通过软链接访问目录。

#历遍所有目录
for w_path, w_dirs, w_files in os.walk(input_path):
    for walk_dirs in w_dirs:
        print(os.path.join(w_path, walk_dirs))
    for walk_files in w_files:
        #合并路径和文件名称
        files_all = os.path.join(w_path, walk_files)
        #str.endswith() str.startswith() 以什么开头，以什么结尾
        if files_all.endswith('.sh') == True:
            print(files_all)

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


print('===================================================')
for w_path, w_dirs, w_files in os.walk(input_path):
    for walk_files in w_files:
        all_file_path3 = os.path.join(w_path, walk_files)
        #定义匹配模式,re.I忽略大小写
        pattern = re.compile(r'\.sh$',re.I)
        #查找
        if pattern.search(all_file_path3):
            print(all_file_path3)

