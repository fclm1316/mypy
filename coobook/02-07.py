#!/usr/bin/python3
#coding:utf-8
#最短匹配模式,贪婪匹配
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
#无法查找"" 中的匹配内容
str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))
