#!/usr/bin/env python3
import os
import linecache
import re
file = 'txt/sh.txt'
print_file1 = linecache.getlines(file)
print('文本一共有 ： {0:d}  行'.format(len(print_file1)))
num_1 = 1
while num_1 <= len(print_file1):
    lines = linecache.getline(file,num_1)
    print('第 {0:d} 行内容是：{1:s}'.format(num_1,str(lines)))
    pattern = re.compile('=')
    if pattern.search(lines) :
        print('本行有等于号')
    else:
        print('本行没有')
    num_1 = num_1 +1
    print('+++++++++++++++')
linecache.clearcache()
#linecache.checkcache(file)
#linecache.updatecache(file)
new_txt = 'txt\\new_sh.txt'
if os.path.exists(new_txt):
    os.remove(new_txt)
#去掉空白行
with open(file,'r',newline='') as fileread:
    fd = fileread.readlines()
    for line in fd:
        #line = line.strip('\n')
        #print(line)
        #\n 占据两个字符
        if len(line) > 2:
            #print(len(line))
            with open(new_txt,'a') as filewrite:
                filewrite.writelines(line)
