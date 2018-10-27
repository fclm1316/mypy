#!/usr/bin/python3
#coding:utf-8
#匿名函数
add = lambda x ,y:x + y
print(add(2,3))
print(add('hello','world'))
# def add(x,y):
#     return x + y
names = ['Clark Kent','bruce wayne','diana prince','barry allen',
         'hal jordan','oliver Queen','arthur curry','j\'Onn j\'Onzz',
         'victor stone']
#排序，将传入的for  aa  in  list  ,在切片取后面值，并按小写排序
sort_name1 = sorted(names,key=lambda name:name.split()[-1].lower())
sort_name3 = sorted(names,key=lambda name:name.split()[0].lower())
sort_name2 = sorted(names,key=lambda name:name.split()[-1])
print(sort_name1)
print(sort_name2)
print(sort_name3)

###??????????????????############
