#!/usr/bin/python3
#coding:utf-8
import functools
#偏函数 传入2进制数，输出十进制
int2 = functools.partial(int,base=2)
print(int2('11'))

def int2(x,base=2):
    return int(x,base)

print(int('11',base=2))



if __name__ == "__main__":
    pass