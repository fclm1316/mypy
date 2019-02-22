#!/usr/bin/python3
#coding:utf-8
import bisect
#序列类型,已排序的列，插入数据
#二分插入、查找.默认使用right
inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,2)
bisect.insort(inter_list,4)
bisect.insort(inter_list,6)
bisect.insort(inter_list,5)
bisect.insort(inter_list,1)

print(inter_list)
#0 1 2 3 right
print(bisect.bisect(inter_list,3))
