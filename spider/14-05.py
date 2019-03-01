#!/usr/bin/python3
#coding:utf-8
import time,threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import requests

def putong_put(queue, input_url):
    for i in range(2,48):
        queue.put('{input_url}_{i}.html'.format(input_url=input_url,i=i))


def putong_get(queue):
    for i in range(2,48):
        item = queue.get()
        print(item)

if __name__ =="__main__":
    input_url = "http://www.123.com/123/"
    #定义队列
    putong_queue = Queue()
    #启动线程，放入地址
    thread_queue = threading.Thread(target=putong_put, args=(putong_queue, input_url,))
    thread_queue.start()

    time.sleep(3)
    #建立线程池
    executor = ThreadPoolExecutor(max_workers = 3)
    #执行线程,putong_get列表形式
    all_task = [executor.submit(putong_get(putong_queue))]

