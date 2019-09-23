#!/usr/bin/python3
#coding:utf-8
#碰到异常时，取消任务

import asyncio
import time

async def get_html(sleep_time):
    print('wating')
    await asyncio.sleep(sleep_time)
    print("done after {}".format(sleep_time))

if __name__ == "__main__":
    task1 = get_html(2)
    task2 = get_html(2)
    task3 = get_html(2)

    tasks = [task1,task2,task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        #获得当前全部任务
        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            print('cancel task')
            print(task.cancel())
        #     停止loop ,和close是由区别的，stop标志状态
        loop.stop()
        #必须run_forever
        loop.run_forever()
    finally:
        loop.close()


