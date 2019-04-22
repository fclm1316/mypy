#!/usr/bin/python3
#coding:utf-8
class Mydict(dict):
    def __setitem__(self, key, value):
        #调用父类
        super().__setitem__(key,value*2)

#没有继承
my_dict = Mydict(one=1)
print(my_dict)
#继承父类
my_dict['one'] = 1
print(my_dict)

from collections import UserDict
class Mydict(UserDict):
    def __setitem__(self, key, value):
        #调用父类
        super().__setitem__(key,value*2)
#集成父类
my_dict = Mydict(one=1)
print(my_dict)

from collections import defaultdict
my_dict = defaultdict(dict)
my_value = my_dict["aa"]
print(my_value)