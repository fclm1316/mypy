#!/usr/bin/env python3
import sys
import os
import glob
input_path = sys.argv[1]
all_file_path = glob.glob(os.path.join(input_path,'*.txt'))
print('所有文件1：')
all_files = os.listdir(input_path)
print(all_files)
print('所有文件2：')
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
# topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
# onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
# followlinks -- 设置为 true，则通过软链接访问目录。
for root,dirs,files in os.walk(input_path):
    for walk_dirs in dirs:
        print(os.path.join(root,walk_dirs))
    for walk_files in files:
        print(os.path.join(root,walk_files))

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
