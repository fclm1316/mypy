#!/usr/bin/python3
#coding:utf-8
#全局解释器锁 global interpreter lock
#gil 会根据执行的字节码时间片或者行数释放，或者时 I/O 操作时
import threading
total = 0
def add():
    global total
    #要够大，不然是 0
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -=1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)
