#!/usr/bin/python3
#coding:utf-8
import array
a =list()
#array 和 list 的一个重要区别，array只能存放指定的数据类型,array效率更高,list灵活
#指定整型
my_array = array.array('i')
my_array.append(1)
my_array.append('aa')