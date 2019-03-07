#!/usr/bin/python3
#coding:utf-8
#传统函数调用 A -> B ->C
#需要一个可以暂停的函数，并且可以在适当的时候恢复函数继续执行
#
def gen_func():
    # yield 1
    #请求时间长，IO操作, 外部将值传递回来 ,产出值（调用方）
    html = yield "http://123/download"
    print(html)
    yield 2
    yield 3
    return 4

#1 生成器不仅可以产出值，还可以接受值


if __name__ == "__main__":
    gen = gen_func()
    #在调用send 必须先启动一次生成器,gen.send(None)
    url =gen.send(None)
    #1 启动生成器有两种 next(), send
    # url = next(gen)
    html ="aa"
    print(gen.send(html)) #send 方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置





    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
