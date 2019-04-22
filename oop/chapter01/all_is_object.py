#!/usr/bin/python3
#coding:utf-8
def ask(name='bobby'):
    print(name)


class Preson:
    def __init__(self):
        print("bobby")

#函数返回函数
def decorator_func():
    print('===========')
    return ask

my_func =ask
my_func("aaa")

my_class = Preson
my_class()

print('-------------------')
obj_list = []
#一次性加入多个 append
obj_list.extend([ask,Preson])
for item in obj_list:
    print(item())
# bobby
# None 由于函数没有返回值，所以是none
# bobby
# <__main__.Preson object at 0x0000022A169DC5C0>

my_ask = decorator_func()
my_ask('tom')
