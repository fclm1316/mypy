#!/usr/bin/python3
#coding:utf-8
my_list = []
my_list.append(1)
my_list.append('a')

from collections import abc

a = [1,2]
c = a + [3,4]
print(c)
#a += (3,4) 元组
#__iadd__ 魔法函数 extend()
a += (3,4)
a.extend(range(3))
a.append([1,2])
a.append((1,2))
print(a)
