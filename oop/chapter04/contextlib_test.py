#!/usr/bin/python3
#coding:utf-8
import contextlib
#使用装饰器简化上下文管理器
@contextlib.contextmanager
def do_something():
    #打开资源
    print('enter')
    #生成器
    yield
    #关闭资源
    print('exit')

with do_something() as d:
    #主体事务
    print('doing')
