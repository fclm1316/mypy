#!/usr/bin/python3
#coding:utf-8
#使用多个界定字符分割字符串
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
new_line = re.split(r';|,\s|\s,',line)
#new_line = re.split(r'[;,\s]\s*',line)
print(new_line)