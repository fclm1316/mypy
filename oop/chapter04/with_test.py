#!/usr/bin/python3
#coding:utf-8
#try except with ???没结果.........
def exe_try():
    try:
        print('code start')
        # raise KeyError
        # return 1
    except KeyError as e:
        print('key error')
        return 2
    else:
        print('other error')
        return 3
    finally:
        print('fanlly')
        #释放资源
        return 4

# if __name__ == "__mian__":
#     a = exe_try()
#     print(a)


#上下文管理器，enter打开资源,exit关闭资源，类似open()
class Sample:
    def __enter__(self):
        #打开资源
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #关闭资源
        print('exit')

    def do_something(self):
        print('doing')

with Sample() as s:
    s.do_something()


#查阅@contextlib.comtextmanager 装饰器
