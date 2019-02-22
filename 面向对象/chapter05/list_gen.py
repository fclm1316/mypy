#!/usr/bin/python3
#coding:utf-8
#列表生成式
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)

print(odd_list)

new_list = [i for i in range(21) if i%2 == 1]
print(new_list)

def hadle_item(item):
    return item * item

new_list = [hadle_item(i) for i in range(21) if i%2 == 1]
print(new_list)


#生成器
new_gen = (i for i in range(21) if i%2 == 1)
print(type(new_gen))
#转换成列
new_list = list(new_gen)
print(type(new_list))


#字典推到式
#将字典中的key value 调换
my_dict = {'aa':11,'bb':22,'cc':33}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)


#集合推导式
# my_set = set(my_dict.keys())
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)
