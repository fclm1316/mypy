#!/usr/bin/python3
#coding:utf-8
#解压可迭代对象赋值给多个变量
#压缩后两位
record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
name,email,*phone_number = record
print(name)
print(email)
print(phone_number)
print('-------------------------------------------------')
#压缩前几位
*trailing,current = [10,8,7,1,9,5,10,3]
print(trailing)
print(current)
print('-------------------------------------------------')
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
print('-------------------------------------------------')
#利用切片压缩
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(":")
print(uname)
print(homedir)
print(sh)
print('-------------------------------------------------')
#废弃
record = ('Acme',50,123.45,(12,18,2012))
name,*_,(*_,year) = record
print(name)
print(year)
