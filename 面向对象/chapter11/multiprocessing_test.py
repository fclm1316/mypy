#!/usr/bin/python3
#coding:utf-8
import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print("sub_progtrss success")
    return n

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html,args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")



    #使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html,args=(3,))
    #等待所有任务结束
    # pool.close()
    # pool.join()
    #获得返回值
    # print(result.get())

    for result in pool.imap(get_html,[1,5,3]):
        print("{} sleep success".format(result))

    #谁先完成谁先打印
    for result in pool.imap_unordered(get_html,[1,5,3]):
        print("{} sleep success".format(result))
