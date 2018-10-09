#!/usr/bin/python3
#coding:utf-8
#查找匹配字符串
#str.find() str.endswith() srt.startswith()
import re
text1 = '11/27/2012'
text2 = 'Nov 27,2012'
#\d 数字
if re.match(r'\d+/\d+/\d',text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d',text2):
    print('yes')
else:
    print('no')

#match() 从字符串开始匹配，任一部位匹配findall()
datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. Pycon starts 3/13/2013 .'
print(datepat.findall(text))
#利用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
#分组格式化时间
for month,day,year in datepat.findall(text):
    print('{0:s}-{1:s}-{2:s}'.format(year,month,day))
    print('{}-{}-{}'.format(year,month,day))
