#!/usr/bin/python3
#coding:utf-8
def gen_func():
    try:
        yield "http://123.com/123"
    except Exception as e:
        pass
    yield 2
    yield 3
    return 'aa'

if __name__ == "__main__":
    gen=gen_func()
    print(next(gen))
    gen.throw(Exception,'download error')
    print(next(gen))
    #仍一个异常
    gen.throw(Exception,'download error')
