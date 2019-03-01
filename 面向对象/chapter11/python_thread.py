#!/usr/bin/python3
#coding:utf-8
#io操作来说，多线程和多进程差别不多

import time
import threading

def get_detail_html(url):
    #获得文章详情页
    print('get detail html started')
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    #获得文章列表页
    print('get detail url started')
    time.sleep(4)
    print("get detail url end")

class GetDetailHtml(threading.Thread):
    #d调用父类
    def __init__(self,name):
        super().__init__(name=name)
        #重新run()方法
    def run(self):
        print('get detail html started')
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(4)
        print("get detail url end")




if __name__ == "__main__":
    #target 传递函数名，不要传递函数调用,参数args(url)
    # thread1 = threading.Thread(target=get_detail_html,args=("",))
    # thread2 = threading.Thread(target=put_detail_url,args=("",))
    # start_time = time.time()
   #守护线程,setDemon,，子线程退出时，再关闭主线程
    # thread1.setDaemon(True)
    # thread1.start()
    # thread2.start()

    #全部线程结束后再关闭主线程
    # thread1.join()
    # thread2.join()

    #三个线程，主线程,需要join,主线程退出时，子线程退出
    # print("last time :{}".format(time.time()-start_time))

    thread3 = GetDetailHtml("get_detal_html")
    thread4 = GetDetailUrl("get_detal_url")
    start_time = time.time()

    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()
    print("last time :{}".format(time.time()-start_time))
