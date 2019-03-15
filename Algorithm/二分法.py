#!/usr/bin/python3
#coding:utf-8
#二分排序
def binary_searcg(list,item):
    low = 0
    #获得列的长度,列是从 0 开始
    high = len(list) - 1  #9
    while low <= high:
        print(list)
    #如果（low + high）不是偶数，Python自动将mid向下取数
        mid = int((low + high) / 2)   #(0+9)/2=4
        #获得中间值
        print('mid 数值是 {0:d}'.format(mid))
        #切片,猜测中间值
        guess = list[mid]  #4
        print('guess 切片数值是 {0:d}'.format(guess))
        #如果中间值等于 传入参数
        if guess == item :
            #打印中间值
            print('猜测的数值在第 {0:d} 位'.format(mid))
            return mid
        #如果中间值大于猜测值
        if guess > item :  #4>3
            # 最顶
            high = mid  - 1  #3
            print('high 重新取数值是 {0:d}, low 值是 {1:d}'.format(high,low))
            print('-----')
        else:
            low = mid + 1  # 1+1
            print('high 值是{0:d}, low 重新取数值是 {1:d}'.format(high,low))
            print('-----')
    return None

my_list = range(0,19987,7)
#print(binary_searcg(my_list,3))
print(binary_searcg(my_list,63))
