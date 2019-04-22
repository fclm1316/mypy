#!/usr/bin/python3
#coding:utf-8
class A:
    #aa类变量
    aa = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(2,3)
#修改类属性,类变量
A.aa = 100
#实例a,aa(),实例变量
a.aa = 200
print(a.x,a.y,a.aa)
print(A.aa)
#AttributeError: type object 'A' has no attribute 'x'
# print(A.x)

