#!/usr/bin/python3
#coding:utf-8
#自省是通过一定的机制查询到对象的内部结构
from class_method import Date
class Person:
    '''
    人
    '''
    name = 'user'

class Student(Person):
    def __init__(self,school_name):
        self.school_name = school_name


if __name__ =='__main__':
   user = Student('haha')
   #打印属性
   print(user.__dict__)
   print(Person.__dict__)
   #mro 向上查找
   print(user.name)
   #只有属性名称，没有值
   print(dir(user))
