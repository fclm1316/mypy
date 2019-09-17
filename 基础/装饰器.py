#!/usr/bin/python3
#coding:utf-8
import functools
#返回函数
def mylog(func):
    # 接收任意值
    def wrapper(*args,**kwargs):
        #打印__name__函数名
        print('call {0:s}()'.format(func.__name__))
        #调用原始函数
        return func(*args,**kwargs)
    return wrapper

@mylog
def now():
    print('20190917')

# now = log(now)
now()


# 装饰器传参
def log(text):
    def decorator(func):
        # wrapper__name = func.__name__
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('{0:s} {1:s}()'.format(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print('20190917')
# now = log('execute')(now)
now()

