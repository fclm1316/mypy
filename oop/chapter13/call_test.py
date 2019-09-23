#!/usr/bin/python3
#coding:utf-8
import asyncio

def callback(sleep_time):
    print("sleep {} sucess".format(sleep_time))

def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #获得循环内的时间
    now = loop.time()
    loop.call_soon(callback,2)
    #使用loop.stop停止 永不停止的loop
    # loop.call_soon(stoploop,loop)
    #永不停止loop
    # loop.run_forever()
    loop.call_later(3,callback,3)
    loop.call_at(now+5,callback,5)
    # 使用loop.stop停止 永不停止的loop
    loop.call_at(now+6,stoploop,loop)
    # 永不停止loop
    loop.run_forever()
