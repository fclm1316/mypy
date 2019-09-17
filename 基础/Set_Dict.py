#!/usr/bin/python3
#coding:utf-8
# dict 通过 key值hash计算，保存在内存中，可以快速找到
# set 只保存key值，且不可重复
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d['Adam']=99
print(d['Adam'])
# print(d['Jack'])
print(d.get('Thoms'))
# 通过get获得值
print(d.get('Thoms',-1))
d.pop('Bob')
print(d)

s1 = set([1,2,3,5])
s2 = set([2,4,5,7,9])
print(s1&s2)
print(s1|s2)

if __name__ == "__main__":
    pass