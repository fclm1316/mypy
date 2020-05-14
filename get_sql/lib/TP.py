#encoding:utf-8
import threading
import contextlib
import time,sys
from Queue import Queue
sys.path.append("..")
from lib.logger import log

log = Log.make_logger()
class ThreadPool(object):
    def __init__(self,max_num):
        self.StopEvent = 0
        self.q = Queue()
        self.max_num = max_num
        self.terminal = False
        self.generate_list = []
        self.free_list = []

    def run(self,func,args,callback=None):
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        task = (func,args,callback,)
        self.q.put(task)

    def generate_thread(self):
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        currnet_thread = threading.current_thread
        self.generate_list.append(currnet_thread)

        event = self.q.get()
        while event != self.StopEvent:
            func,arguments,callback = event
            try:
                result = func(*arguments)
                status = True
            except Exception as e:
                status = False
                result = e
                log.error("调用函数执行错误 {}").format(result)

            if status:
                if callback is not None:
                    try:
                        callback(status,result)
                    except Exception as e:
                        log.error("回调函数执行错误 {}").format(e)

            if self.terminal:
                event = self.StopEvent
            else:
                with self.worker_state(self.free_list,currnet_thread):
                    event = self.q.get()
        else:
            self.generate_list.remove(currnet_thread)

    def close(self):
        num = len(self.generate_list)
        while num:
            self.q.put(self.StopEvent)
            num -=1

    def terminate(self):
        self.terminal = True
        while self.generate_list:
            self.q.put(self.StopEvent)
        self.q.empty()

    def active_count(self):
        thread_count = threading.activeCount()
        return thread_count

    def active_name(self):
        thread_name = threading.enumerate()
        return list(thread_name)

    @contextlib.contextmanager
    def worker_state(self,free_list,current_thread):
        free_list.append(current_thread)
        try:
            yield
        finally:
            free_list.remove(current_thread)

if __name__ == '__main__':
    def work(i):
        time.sleep(5)

    pool = ThreadPool(10)

    for item in range(20):
        pool.run(func=work,args=(item,))

    pool.close()
    print(pool.active_name())
