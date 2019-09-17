#!/usr/bin/python3
#coding:utf-8
list_a = [x for x in range(10)]
print(list_a)
list_b = [x*x for x in range(10)]
print(list_b)
list_c = [x*y for x in range(10) for y in range(10)]
print(list_c)
list_d = [x*y for x in range(10) for y in range(10) if x*y % 2 == 0 ]
print(list_d)

if __name__ == "__main__":
    pass