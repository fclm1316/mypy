#!/usr/bin/python3
#coding:utf-8
#控制线程数量
import threading
import time


class Htmlspider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        #运行结束后释放
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            #此处加锁
            self.sem.acquire()
            html_thread = Htmlspider("http://123.com/{}".format(i),self.sem)
            #这里部门释放锁,在线程中释放锁
            html_thread.start()

if __name__ == "__main__":
    #定义所锁数量
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()