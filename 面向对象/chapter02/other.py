#!/usr/bin/python3
#coding:utf-8
class Nums(object):
    def __init__(self,num):
        self.num = num
    #附加abs(),使得外部可用。
    def __abs__(self):
        return abs(self.num)

my_num = Nums(-9)
print(abs(my_num))

class MyVector(object):
    #初始化
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #循环调用class MyVector,二次传入.....
    def __add__(self, other):
        re_vector = MyVector(self.x + other.x,self.y + other.y)
        return re_vector
    def __str__(self):
        #打印字符串
        return "x:{x},y:{y}".format(x=self.x,y=self.y)

vec1 = MyVector(1,2)
vec2 = MyVector(2,3)
vec3 = MyVector(3,4)

print(vec1+vec2+vec3)
