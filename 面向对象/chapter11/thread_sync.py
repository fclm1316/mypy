#!/usr/bin/python3
#coding:utf-8
#全局解释器锁 global interpreter lock
#锁
import threading
from threading import Lock,RLock
#声明一个锁,锁影响性能
lock = Lock()
total = 0
# lock = RLock
# Rlock 再同一个线程中可重入的锁

def add():
    global total
    global lock
    #要够大，不然是 0
    for i in range(1000000):
        #获得锁，锁住线程
        lock.acquire()
        # lock.acquire()
        total += 1
        #必须释放锁
        print(total)
        lock.release()

def desc():
    global total
    for i in range(1000000):
        #如果没有释放，这里将等待获得锁，死锁
        lock.acquire()
        total -=1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
#线程启动有顺序,相互等待对方锁
# A(a,b)
#acquire (a)
#acquire (b)
# B(b,a)
#acquire (b)
#acquire (a)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
