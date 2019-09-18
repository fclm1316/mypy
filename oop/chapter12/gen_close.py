#!/usr/bin/python3
#coding:utf-8
def gen_func():
    html = yield "http://123/download"
    print(html)
    yield 2
    yield 3
    return 4



if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    #关闭
    gen.close()
    print(next(gen))
