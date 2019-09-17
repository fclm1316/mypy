#!/usr/bin/python3
#coding:utf-8
#可迭代，迭代器(__next__)
from collections.abc import Iterable,Iterator
a = [1,2]
#可迭代
print(isinstance(a,Iterable))
#不是迭代器
print(isinstance(a,Iterator))

iter_rator = iter(a)
print(isinstance(iter_rator,Iterator))
#生成器 generator。yield 可迭代的对象 Iterable .可以通过for 循环的为生成器 list dict str.不但可以用作for循环，还可以用next()
#不断调用直到最后抛出StopIteration错误表示无法返回下一个值
#isinstance([],Iterable) 判断是否可迭代
#isinstance((),Iterable)
#isinstance({},Iterable)

#生成器都是 迭代器（iterator）的对象，list dict str 是可迭代的对象(Iterable)，但不是迭代器
#迭代器可以是全体自然数 ， 但是 list  不行。
#--------------------------------
#            迭代器              |
#|-------------|-----------------
#|   生成器     | iter(list)     |
#|   yield     | iter(dict)     |
#|generator fun| iter(str)      |
#-------------------------------