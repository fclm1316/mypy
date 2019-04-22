#!/usr/bin/python3
#coding:utf-8
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

#Series 一维数组 index , values
s = Series([3,2,4,5,7],index=['a','b','c','d','o'])
print(s)
print(s.index)
print(s.values)
#值 排序
print(s.sort_values())
print('提取 index')
print(s['c'])
#把标签放入
print(s[['c','o']])
print('提取 values')
#切片
print(s[0:4:2])
#赋值,series 对数据的引用，修改数据，将修改series
s['o'] = 10
print(s)

#筛选元素,对于值的筛选
print('s 大于 2')
print(s[s>2])
#运算
print('--------')
print(s*3)
print(np.log(s))

print('--------')
serd = Series([1,2,3,4,4,5,6,7,7,3],index=['a','b','c','d','e','f','g','h','i','j'])
print(serd)
#去重复,返回list
print(serd.unique())
#统计重复
print(serd.value_counts())
#判断所属关系,布尔值
print(serd.isin([3,5]))
print(serd[serd.isin([3,5])])

#简单判断 NaN 缺失数据 serd.isnull() notnull
print(serd.isnull())
print('--------------')
mydict = {'red':100,'blue':200,'yellow':300,'orange':500}
myseries = Series(mydict)
print(myseries)
#缺失 自动填补
colors = ['red','blue','yellow','orange','green']
myseries = Series(mydict,index=colors)
print(myseries)
print(myseries.notnull())
print('--------------')
#series 运算，对相同的保留运算，不同的NaN ，如何保留?
mydict2 = {'red':100,'yellow':200,'black':300}
myseries2 = Series(mydict2)
print(myseries + myseries2)


print('--------------')
print('==============')
data = {'color':['blue','green','yellow','red','white'],'boject':['ball','pen','pencil','paper']}

