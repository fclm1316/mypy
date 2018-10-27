#!/usr/bin/python3
#coding:utf-8
#函数的某些参数强制使用关键字参数传递
#定义接受多个位置参数得函数，指定关键字参数
def mininum(*values,clip=None):
    #取最小值
    m = min(values)
    #如果关键字参数不为空
    if clip is not None:
        #关键字
        m=clip if clip > m else m
         # if clip >m:
         #     m=clip
         # else:
         #     m
    return m
print(mininum(1,5,2,-5,10))
print(mininum(1,5,2,-5,10,clip=0))