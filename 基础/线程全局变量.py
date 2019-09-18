#!/usr/bin/python3
#coding:utf-8
#线程之间变量传递
import threading
local_school = threading.local()

def process_student():
    #可绑定其他值
    std = local_school.student
    #获得线程的名字
    print('Hello , {0:s} in {1:s}'.format(std,threading.current_thread().name))

def process_thread(name):
    #绑定线程的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Bat',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Dog',),name='Thread-B')
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
#这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
t1.start()
t2.start()
t1.join()
t2.join()


if __name__ == "__main__":
    pass