#!/usr/bin/python3
#coding:utf-8
#格式化字符串  字符串对齐
text = 'Hello World'
print(text.ljust(20,'='))
print(text.rjust(20,'*'))
print(text.center(20,'^'))
#使用format()
print('=====================')
print(format(text,'>20'))
print(format(text,'<20'))
print(format(text,'^20'))
print('=====================')
print(format(text,'=>20s'))
print(format(text,'-<20s'))
print(format(text,'*^20s'))
print('{0:=>10s} {1:0<12d} {2:*^14s}'.format('hello',11,'end'))

x = 1234567890.987654321
print(format(x,'0.2f'))
print(format(x,'20.1f'))
print(format(x,','))
print(format(x,'e'))
print(format(x,'E'))
# 3.1415926	{:.2f}	3.14	保留小数点后两位
# 3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
# -1	{:+.2f}	-1.00	带符号保留小数点后两位
# 2.71828	{:.0f}	3	不带小数
# 5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
# 5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
# 10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
# 1000000	{:,}	1,000,000	以逗号分隔的数字格式
# 0.25	{:.2%}	25.00%	百分比格式
# 1000000000	{:.2e}	1.00e+09	指数记法
# 13	{:10d}	        13	右对齐 (默认, 宽度为10)
# 13	{:<10d}	13	左对齐 (宽度为10)
# 13	{:^10d}	    13	中间对齐 (宽度为10)
# 11
# '{:b}'.format(11)    1011
# '{:d}'.format(11)    11
# '{:o}'.format(11)    13
# '{:x}'.format(11)     b
# '{:#x}'.format(11)    0xb
# '{:#X}'.format(11)    0XB
# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
#
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
#
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
