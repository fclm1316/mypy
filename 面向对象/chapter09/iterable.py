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
