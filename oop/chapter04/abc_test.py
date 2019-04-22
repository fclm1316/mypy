#!/usr/bin/python3
#coding:utf-8
#检查某个类是否有某种方法
class Company():
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(['bobby1','bobby2'])
#判断是否有len()
print(hasattr(com,'__len__'))
#在某些情况下希望判定某个对象类型
from collections.abc import Sized
print(isinstance(com,Sized))

