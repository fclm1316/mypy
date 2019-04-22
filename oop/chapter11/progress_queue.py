#!/usr/bin/python3
#coding:utf-8
import time
from multiprocessing import Process,Queue,Manager,Pool,Pipe
# 多线程可使用，多进程不行
# 共享全局变量不能多进程
#multiprocessing queue 不能用在pool进程池
# pool 中进程间通讯需要 Manager() 实例化

#多线程：全局变量, Queue
#多进程：Manager().Queue() ，Pipe() 。


# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer,args=(queue,))
#     my_consumer = Process(target=consumer,args=(queue,))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_consumer.join()
#     my_producer.join()

# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     #pool中的进程间使用Manager()
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer,args=(queue,))
#     pool.apply_async(consumer,args=(queue,))
#
#     pool.close()
#     pool.join()

# def producer(pipe):
#     pipe.send = ('aa')
#
# def consumer(pipe):
#     print(pipe.recv())
#
#
# if __name__ == "__main__":
#     R_pipe , S_pipe = Pipe()
#     #pipe 性能高queue
#     #pipe只能适合用户两个进程间的通讯
#     my_producer = Process(target=producer,args=(S_pipe,))
#     my_consumer = Process(target=consumer,args=(R_pipe,))
#
#     my_producer.start()
#     my_consumer.start()
#     my_consumer.join()
#     my_producer.join()

def add_data(p_dict,key,value):
    p_dict[key]  = value

if __name__ == "__main__":
    #Manager() 还有字典，列表，队列等
    #共享字典，内存共享
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data,args=(progress_dict,"aa",1))
    second_progress = Process(target=add_data,args=(progress_dict,"bb",2))

    first_progress.start()
    second_progress.start()

    first_progress.join()
    second_progress.join()

    print(progress_dict)
