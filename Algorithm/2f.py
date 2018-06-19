#!/usr/bin/python3
#coding:utf-8
def binary_searcg(list,item):
    low = 0
    high = len(list) - 1  #9
    while low <= high:
    #如果（low + high）不是偶数，Python自动将mid向下取数
        mid = int((low + high) / 2)   #(0+9)/2=4    # (0+3)/2=1
        print('mid 数值是 {0:d}'.format(mid))
        guess = list[mid]  #5 #2
        print('guess 数值是 {0:d}'.format(guess))
        if guess == item :
            print('猜测的数值在第 {0:d} 位'.format(mid))
            return mid
        if guess > item :  #5>3   #2<3
            high = mid  - 1  #3
            print('high 重新取数值是 {0:d}'.format(high))
            print('-----')
        else:
            low = mid + 1  # 1+1
            print('low 重新取数值是 {0:d}'.format(low))
            print('-----')
    return None

my_list = range(0,1000,3)
#print(binary_searcg(my_list,3))
print(binary_searcg(my_list,300))
