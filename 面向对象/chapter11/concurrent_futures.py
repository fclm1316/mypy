#!/usr/bin/python3
#coding:utf-8
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
import time

from concurrent.futures import Future
#未来对象,task的返回结果
#当一个线程完成的时候，主线程能立即知道
#线程完成后，获得线程的返回值

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=3)
#通过submit函数提交执行的函数到线程池中,submit 是立即返回
#使用函数名称，而不是实例化
# task1 = executor.submit(get_html,(3))
# task2 = executor.submit(get_html,(2))

#获取已成功的返回值
urls = [3,4,5,6,7,8,9,10]
#列表化url
all_task =[executor.submit(get_html,(url)) for url in urls]
#as_completed 返回迭代yield
for future in as_completed(all_task):
    #获得值
    data = future.result()
    print("get {} page result".format(data))

print("-------------------------------------------")

#更加好的方法
for data in executor.map(get_html,urls):
    print("get {} page result".format(data))

# 等待所有线程结束
#wait(all_task)
# 等待第一个线程结束
# wait(all_task,return_when=FIRST_COMPLETED)

# print(task1.done())
# #无法取消 正在经行 或者 执行完毕 的线程,只能取消等待的线程
# print(task1.cancel())
# time.sleep(3)
# print(task1.done())
# #获得线程的返回值
# print(task1.result())
