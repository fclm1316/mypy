#!/usr/bin/python3
#coding:utf-8
#通过queue方式同步
import time
import threading
from queue import Queue
#源码注释


def get_detail_html(queue):
    while True:
        #阻塞方法get(),timeout,block
        url = queue.get()
        print('get detail html started')
        print(url)
        time.sleep(2)
        print("get detail html end")

def put_detail_url(queue):
    #获得文章列表页
    print('get detail url started')
    # time.sleep(4)
    for i in range(20):
        #队列丢消息
        #put_nowait
        queue.put('https://123.com/{id}'.format(id=i))
    print("get detail url end")




if __name__ == "__main__":
    #最大队列容量
    detail_url_queue = Queue(maxsize=10000)
    thread_detail_url = threading.Thread(target=put_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        html_thead = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
        html_thead.start()

