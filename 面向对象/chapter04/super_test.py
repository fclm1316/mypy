#!/usr/bin/python3
#coding:utf-8
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        #调用mro 算法中的父类,由算法判定广度优先，还是深度优先
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(B,C):
    def __init__(self):
        print('D')
        super().__init__()


if __name__ == "__main__":
    #广度优先
    print(D.__mro__)
    d = D()