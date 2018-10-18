#!/usr/bin/python3
#coding:utf-8
#格式化长字符串，指定列宽
import textwrap
import os
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s,70))
print('-------------------------')
print(textwrap.fill(s,40))
print('-------------------------')
print(textwrap.fill(s,40,initial_indent='    '))
print('-------------------------')
print(textwrap.fill(s,40,subsequent_indent='    '))
print('-------------------------')
#获得终端的大小
Terminal_size = os.get_terminal_size().columns
Terminal_size1 = os.get_terminal_size().lines
print(Terminal_size)
print(Terminal_size1)
