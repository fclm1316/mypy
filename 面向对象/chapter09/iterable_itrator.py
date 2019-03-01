#!/usr/bin/python3
#coding:utf-8
from collections.abc import Iterator
class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

class MyIterator(Iterator):
    def __init__(self,employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代器的逻辑，不能切片
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index +=1
        return word



if __name__ == "__main__":
    company = Company(["tom","bob","jane"])
    #for 自动调用内置 iter()
    # iter(company)
    for item in company:
        print(item)