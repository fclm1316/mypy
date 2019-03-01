#!/usr/bin/python3
#coding:utf-8
import threading

# class XiaoAi(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name='小爱')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 好啊".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name='天猫精灵')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 小爱同学".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧".format(self.name))
#         self.lock.release()

from threading import Condition
import time
class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            time.sleep(1)
            print("{} : 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 好啊".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 1".format(self.name))
            self.cond.notify()

            self.cond.wait()
            time.sleep(1)
            print("{} : 2".format(self.name))
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self,cond):
        #调用父类,定义self.name
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            #锁通知
            self.cond.notify()
            time.sleep(1)
            print("{} : 小爱同学".format(self.name))
            #锁等待通知
            self.cond.wait()

            self.cond.notify()
            time.sleep(1)
            print("{} : 我们来对古诗吧".format(self.name))
            self.cond.wait()

            self.cond.notify()
            time.sleep(1)
            print("{} : A".format(self.name))
            self.cond.wait()

            self.cond.notify()
            time.sleep(1)
            print("{} : B".format(self.name))
            self.cond.wait()

if __name__ == "__main__":
    #定义 condition
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    #启动顺序很重要，tiaomao notify() 信号已发出，但xiaoai线程还未启动
    # tianmao.start()
    # xiaoai.start()
    xiaoai.start()
    tianmao.start()
