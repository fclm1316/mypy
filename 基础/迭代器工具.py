#!/usr/bin/python3
#coding:utf-8
import itertools

#无限迭代器
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10 , natuals)
#使用tabewhile 控制次数
print(list(ns))
# for i in natuals:
#     print(i)
#1~无限

# cs = itertools.cycle('ABCD')
# for i in cs:
#     print(i)
#无限循环 A-B-C-D-A-B

# ns = itertools.repeat('ABCD',9)
# for i in ns:
#     print(i)
#循环 ABCD ,第二个参数 为次数

#将可迭代的对象粘合在一起
a = ['1','s','jas','333']
b = ['2','as']

for c in itertools.chain(a,b):
    print(c)

#相邻且重复的元素挑选
#忽略大小写,实际转为大写
for key,group in itertools.groupby('AAABBBCCCCAAAaaabbbbcccdggf',lambda x:x.upper()):
    print(key,list(group))



print('========================')
#从列中选出任意指定长度的元素，组成排序元组
for i in itertools.permutations([1,2,3,3,5,7],2):
    print(i)

print('------------------------')

for i in itertools.combinations([1,2,3,3,5,7],2):
    print(i)

print('------------------------')

#带重复
for i in itertools.combinations_with_replacement([1,2,3,3,5,7],2):
    print(i)

#获取三个数，之和为50
data = range(100)
def num_sum(data_list,count):
    for num in itertools.combinations(data_list,count):
        if sum(num) == 50:
            print(num)


s = num_sum(data,3)
print(s)

if __name__ == "__main__":
    pass