#!/usr/bin/python3
#coding:utf-8
#函数里面含有 yield 关键字,生成器函数
def gen_func():
    yield 1
    yield 2
    yield 3
#斐波拉契 0 1 1 2 3 5 8 13 21 34 55
#惰性求值（延迟求值）

def fib(index):
    if index <= 2:
        return 1
    else:
        #循环调用
        return fib(index-1) + fib(index-2)

print(fib(10))

def fib2(index):
    #当数据量很大时，消耗内存
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
        n +=1
    return re_list

print(fib2(10))


def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b ,a+b
        n += 1

for data in gen_fib(10):
    print(data)


def func():
    return 1

if __name__ == '__main__':
    gen = gen_func()
    for value in gen:
        print(value)
    # re = func()
