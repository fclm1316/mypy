#!/usr/bin/python3
#coding:utf-8
#删除字符串中不需要的字符
s = '    ----=====hello   world-----======   \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.strip(' -'))
#生成器
# with open(filename) as f :
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)

