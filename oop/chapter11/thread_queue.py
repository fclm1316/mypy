#!/usr/bin/python3
#coding:utf-8
import time
import threading

detail_url_list = []

def get_detail_html(url):
    #获得文章详情页
    global detail_url_list
    url = detail_url_list.pop
    #for 单个读取list中的，没有多线程
    # for url in detail_url_list:
    print('get detail html started')
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    #获得文章列表页
    global detail_url_list
    print('get detail url started')
    time.sleep(4)
    for i in range(20):
        detail_url_list.append("http://123.com/{id}".format(di=i))
    print("get detail url end")



#获得页面，再交给有另一线程获得详情
#使用共享变量
#开启多个线程

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_url)
    thread2 = threading.Thread(target=get_detail_html)
    thread3 = threading.Thread(target=get_detail_html)
    start_time = time.time()

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("last time :{}".format(time.time()-start_time))