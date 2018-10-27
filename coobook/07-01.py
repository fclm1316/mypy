#!/usr/bin/python3
#coding:utf-8
#实参--位置参数
def avg(first,*rest):
    return((first + sum(rest)) / (1+len(rest)))
print(avg(1,2,3))
print(avg(2,4,6,8))
#形参--位置参数
#*实参，只能在位置参数后面  **形参旨在在最后一个参数,关键字参数
#强制关键字参数07-02
def name_age(first_name,last_name,*other_name,**kwargs):
    print(first_name)
    print(last_name)
    if len(other_name) != 0:
        #print('\n'.join(str(x) for x in other_name))
        print(*other_name,sep='\n')
    #print(kwargs)
    for key,values in kwargs.items():
        print('{}={}'.format(key,values))
name_age('Bruce','Wayne','Batman','batman',age=28,human='Y')
name_age('Bruce','Wayne',age=28)
