#!/usr/bin/python3
#coding:utf-8
#有个字典，根据关键字排序。
rows = [
    {'fname':'brian','lname':'jones','uid':1003},
    {'fname':'david','lname':'beazley','uid':1002},
    {'fname':'john','lname':'cleese','uid':1001},
    {'fname':'big','lname':'jones','uid':1004},
]
from operator import itemgetter
row_by_name = sorted(rows,key=itemgetter('fname'))
row_by_uid = sorted(rows,key=itemgetter('uid'))
print(row_by_name)
print(row_by_uid)