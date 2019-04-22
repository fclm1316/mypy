#!/usr/bin/python3
#coding:utf-8
#python 中的垃圾回收的算法采用 引用计数
a = object()
b = a
del a
print(b)
print(a)

class A:
    def __del__(self):
        pass



if __name__ == "__main__":
    pass