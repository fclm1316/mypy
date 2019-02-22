#!/usr/bin/python3
#coding:utf-8
class A:
    pass

#B继承A
class B(A):
    pass

b = B()

#判断b 是不是B的类型
print(isinstance(b,B))
#B()继承了A,寻找继承关系
print(isinstance(b,A))
#在type中并没有继承
print(type(b) is B)
print(type(b) is A)

