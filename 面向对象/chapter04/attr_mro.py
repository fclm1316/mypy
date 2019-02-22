#!/usr/bin/python3
#coding:utf-8
class A:
    name = 'a'
    def __init__(self):
        self.name = 'obj'

a = A()
#实例由下而上查找，先找self.name = 'obj'
#如果找不到，在找name='a'
print(a.name)


#使用C3算法判断
#广度优先搜索
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)

#深度优先搜索
class E():
    pass

class F(E):
    pass

class G():
    pass

class H(G):
    pass

class I(F,H):
    pass

print(I.__mro__)

