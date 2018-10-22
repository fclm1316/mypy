#!/usr/bin/python3
#coding:utf-8
#print() 相关技巧
#输出重定向到文件，文件必须是文本模式打开
#with open('file.txt','r',newline='') as f:
#使用x模式判断文件是否存在 或者os.path.exists()
#with open('file.txt','x',newline='') as f:
#    print('Hello World',file=f)
print('Barry Allen',50,91.5)
print('Barry Allen',50,91.5,sep=',',end="!!!!\n")
for i in range(5):
    print(i)
for i in range(6):
    print(i,end=' ')

f = ('Barry Allen',50,91.5)
#迭代器??
print(':'.join(str(x) for x in f))
print(*f,sep=':')
