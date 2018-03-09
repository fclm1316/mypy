#!/usr/bin/env python3
import linecache
file = 'txt/sh.txt'
print_file1 = linecache.getlines(file)
print('文本一共有 ： {0:d}  行'.format(len(print_file1)))
num_1 = 1
while num_1 <= len(print_file1):
    print('第 {0:d} 行内容是：{1:s}'.format(num_1,str(linecache.getline(file,num_1))))
    num_1 = num_1 +1

