#!/usr/bin/python3
#coding:utf-8
#命名切片，切片的可读性
record = '...........................100....................513.25........'
cost = int(record[27:30]) * float(record[50:56])
print(cost)
SHARES = slice(27,30)
PRICE = slice(50,56)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
items = [0,1,2,3,4,5,6,7,8,9]
a = slice(2,4)
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)
# a = slice(5,10,2)
# a.start
# a.stop
# a.step