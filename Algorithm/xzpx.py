#!/usr/bin/python3
#coding:utf-8
#选择排序
def findSmallest(arr):
    smallest = arr[0]      #获得第一个用来比较的值
    smallest_index = 0      #它的位置是 0 位
    for i in range(1,len(arr)):   #循环比较,获得此列表最小值,和位置
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            print(smallest,smallest_index)
    return smallest_index     #返回位置
def selectionSort(arr):
    newArr = []         #定义空列
    for i in range(len(arr)):   #设置循环
        smallest_index = findSmallest(arr) #获得最小值的位置
        print('---')
        print(smallest_index)
        print('+++')
        newArr.append(arr.pop(smallest_index)) #弹出最小值的位置，并加入新的列表中
        print(newArr)
        print(arr)
    return newArr

print(selectionSort([5,4,6,9,3,2,8,1,7]))
