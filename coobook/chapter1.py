#!/usr/bin/python3
#coding:utf-8
import heapq
from collections import Counter
#1.1 现在有一个包含N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值
#给N 个变量？
#定义的变量的个数和序列元素的个数必须一致
#数字
# p = (4,5)
# x,y = p
# x = 4 ; y = 5
#字符，浮点数，元组
# data = ['acme',50,91.1,(2012,12,21)]
# name ,share, price,date = data
# name = acme ; share = 50 ; price = 91.1 ; date = (2012,12,21)
#字符串
# s = 'Hello'
# a,b,c,d,e = s
# a = 'H';b='e';e='o'
#占位符 ,确保占位符
# data = ['acme',50,91.1,(2012,12,21)]
# _,share,price,_= data

#1.2
#如果一个可迭代对象的元素个数超过变量个数时，会抛出一个ValueError 。那么
#怎样才能从这个可迭代对象中解压出N 个元素出来？
# record = ('dave','dave@example.com','773-555-1212','847-555-1212')
# name,email,*phone_numbers = record
# name = 'dave';email = 'dave@example.com';phone_numbers=['773..','847...']

# *trailing_qtrs,current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
# return avg_comparison(trailing_avg,current_qtr)

records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4)
]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)
for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#形参
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
username,*fileds,homedir,sh = line.split(':')
print(username,homedir,sh)

record = ('ACME',50,123.45,(12,18,2012))
name,*_,(*_,year) = record
print(name,year)
#1.4 查找最大或最小的N个元素
#最大最小 关键字排序
nums = [1,8,2,23,4,-6,3,45,67,-9,-42]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
#如果查找值是最大或者最小 使用 max() min()快
#如果要排序的值和集合大小接近，sorted(item)[:N] 或者是 sorted(item)[-N:] 切片
portfollo = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'APPL','shares':50,'price':345.23},
    {'name':'FB','shares':200,'price':12.9},
    {'name':'HPQ','shares':35,'price':139},
    {'name':'BAB','shares':45,'price':9},
    {'name':'YHOO','shares':45,'price':12.45},
    {'name':'ACME','shares':45,'price':89.2}
]
cheap = heapq.nsmallest(3, portfollo, key=lambda s:s['price'])
expensive = heapq.nlargest(3, portfollo, key=lambda s:s['price'])
print(cheap)
print(expensive)
#查找两个字典的相同点

#切片命名
##########012345678901234567890123456789012345
# record = '003213123l234412323123.23323331286434,'
# cost = int(record[12:13] * float[20:24])
# #cost = 44 * 23.23
# SHARES = slice(20,23)
# PRICE = slice(31,37)
# cost = int(record[SHARES])*float(record[PRICE])

words =[
    'look','into','eyes','my','eyes','look','into','my','eye',
    'the','eyes','the','eyes','the','eyes','not','around','the',
    'eyes',"don't","look",'around','the','eyes','look','into',
    'my','eyes',"you're",'under'
]

words_counts = Counter(words)
top_three = words_counts.most_common(3)
print(top_three)
print(words_counts['not'])
print(words_counts['eyes'])
#增加计数，可以简单的用法加
morewords = ['why','are','you','not','looking','in','my','eyes']
# for word in morewords:
#     words_counts[word] += 1
# print(words_counts['not'])
words_counts.update(morewords)
