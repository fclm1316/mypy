#!/usr/bin/python3
#coding:utf-8
#定义一个又可选参数得函数，直接在函数定义中给参数指定一个默认值，并
#放到参数列表最后
def spam(a,b=42):
    print(a,b)
    print('+++++++++')
print(spam(1))
print('-----------')
print(spam(1,2))


_no_valve = object()
def spam1(a,b=_no_valve):
    if b is _no_valve:
        print('No b value supplied')
#传递空值和不传值是有区别的
print(spam1(1))
print(spam1(1,2))
print(spam1(1,None))
