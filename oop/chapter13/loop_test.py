#!/usr/bin/python3
#coding:utf-8
#事件循环 + 回调(驱动生成器) + epool(IO多路复用)
#asyncio 是python 用于解决异步io编程的一整套解决方案
#tornado gevent twisted(scrapy django channels)
#tornado (实现web服务器)，django + flask (uwsgi + gunicorn + nginx)
#tornado 可以直接部署 ， nginx + tornado
#数据库驱动不行
import asyncio
import time
from functools import partial

# async def get_html(url):
#     print('start get url')
#     #不可以使用time.sleep()
#     await asyncio.sleep(2)
#     print('end get url')
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     #列表
#     task = [get_html('http://123.com') for i in range(100)]
#     # loop.run_until_complete(get_html('http://123.com'))
#     #类似线程池进程池
#     loop.run_until_complete(asyncio.wait(task))
#     print(time.time() - start_time)
#___________________________________________________________________________
#获取协程的返回值
# async def get_html(url):
#     print('start get url')
#     #不可以使用time.sleep()
#     await asyncio.sleep(2)
#     return "hah"
# #调用get_html完成后发送邮件.task返回future值，可接受函数在前
# def callback(url,future):
#     print(url)
#     print('send email')
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     # get_future = asyncio.ensure_future(get_html('http://123'))
#     # loop.run_until_complete(get_future)
#     # print(get_future.result())
#     # 上下同理，在ensure_future 中基于create_task
#     task = loop.create_task(get_html("http://123"))
#     #使用偏函数传递参数值
#     task.add_done_callback(partial(callback,"http://123"))
#     loop.run_until_complete(task)
#     print(task.result())


#__________________________________________________________________


#
async def get_html(url):
    print('start get url')
    print(url)
    #不可以使用time.sleep()
    await asyncio.sleep(2)
    return "hah"
#调用get_html完成后发送邮件.task返回future值，可接受函数在前
def callback(url,future):
    print(url)
    print('send email')

#gather 和 wait 区别
if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    group1 = [get_html("http://123") for i in range(10)]
    group2 = [get_html("http://345") for i in range(10)]
    #分组传递参数 , wait 只能传递一个
    loop.run_until_complete(asyncio.gather(*group1,*group2))
    print(time.time()-start_time)
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # 取消
    # group1.cancel()
    loop.run_until_complete(asyncio.gather(group1,group2))
    print(time.time()-start_time)
