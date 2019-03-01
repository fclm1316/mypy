#!/usr/bin/python3
#coding:utf-8
import threading
from queue import Queue
import time


def mydef_put(queue):
   print("start put")
   #循环放入
   for i in range(5):
      queue.put('数字 {id}'.format(id=i))


def mydef_get(queue):
    #先进先出，只取一个
    print("start get")
    #不停取出
    while True:
        print(queue.get())
        print(queue.qsize())
        time.sleep(1)


if __name__ == "__main__":
    #定义队列的最大长度
   my_queue = Queue(maxsize=300)
   #两个线程放入
   for i in range(2):
        my_thead = threading.Thread(target=mydef_put,args=(my_queue,))
        my_thead.start()
    #一个线程取出
   for i in range(1):
        my_thead1 = threading.Thread(target=mydef_get,args=(my_queue,))
        my_thead1.start()
