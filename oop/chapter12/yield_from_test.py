#!/usr/bin/python3
#coding:utf-8
from itertools import chain
my_list = [1,2,3]
my_dict = {
    "aaa" : "AAA",
    "bbb" : "BBB"
}

def my_chain(*args,**kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value

def my_chain1(*args,**kwargs):
    for my_iterbale in args:
        yield from my_iterbale

#可迭代对象用一个for循环拼接
for value in chain(my_list,my_dict,range(5,10)):
    print(value)

for value in my_chain(my_list,my_dict,range(5,10)):
    print(value)

for value in my_chain1(my_list,my_dict,range(5,10)):
    print(value)

print("===========================")
# yield 与 yield from 区别
def g1(iterable):
    yield iterable

def g2(iterable):
    yield from iterable

for value in g1(range(10)):
    print(value)

for value in g2(range(10)):
    print(value)


def g3(gen):
    yield from gen

def main():
    g = g3()
    g.send(None)
#main 调用方. g1（委托生成器）. gen 子生成器.
#yield from 会在调用方与子生成器之间建立一个双向通道



if __name__ == "__main__":
    pass