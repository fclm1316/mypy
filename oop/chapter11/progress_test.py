#!/usr/bin/python3
#coding:utf-8
#GIL 锁 。多cpu消耗 用多进程(计算)。io操作来说，使用多线程。
#
from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
#简易多线程池

if __name__ == "__main__":
    #在windows 中 多进程必须在if __name__ == "__main__"下
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib,(num)) for num in range(25,35)]
        start_time = time.time()
        #获得完成的线程
        for future in as_completed(all_task):
            #获得返回值
            data = future.result()
            print("exe result : {}".format(data))

        print("last time is : {}".format(time.time()-start_time))

    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib,(num)) for num in range(25,35)]
        start_time = time.time()
        #获得完成的线程
        for future in as_completed(all_task):
            #获得返回值
            data = future.result()
            print("exe result : {}".format(data))

        print("last time is : {}".format(time.time()-start_time))
