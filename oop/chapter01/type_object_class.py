#!/usr/bin/python3
#coding:utf-8
a = 1
class s_a():
    pass

class s_b(s_a):
    pass

def b():
    print('-')

c = b
print(type(a))
print(type(int))
print(type(s_a))
print(s_a.__bases__)
print(object)
print(s_b.__bases__)