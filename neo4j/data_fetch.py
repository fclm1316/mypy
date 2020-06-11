# encoding:utf-8
import asyncio
import pandas as pd
from queue import Queue
from collections import Counter
import time
import json

input_filename = 'D:/data/cbcp_20191011/388.txt'
# input_filename = 'D:/data/cbcp_20191011/test.txt'
q = Queue()
q_dict = Queue()


async def my_test():
    # 对队列中的书记进行统计
    # 再放入新队列中
    # print(q.qsize())
    # print("开始时间")
    start_time = time.time()
    # print('队列转列表')
    list_q = []
    for i in range(q.qsize()):
        list_q.append(q.get())
    # print('统计队列')
    q_dict.put(Counter(list_q))
    end_time = time.time()
    print("转换耗时 : {}".format(end_time - start_time))


async def take_data():
    # 打开文件，限制打开大小，pd获得字段信息，放入队列中
    # 限制队列大小，到达10000时，暂停
    #
    # print('打开文件')
    # data_frame = pd.read_csv(input_filename,encoding='utf-8',low_memory=False,chunksize=10000,delimiter="^",error_bad_lines=False)
    data_frame = pd.read_csv(input_filename, encoding='gb18030', low_memory=False, chunksize=10000, delimiter="|",
                             error_bad_lines=False)
    # print('读取信息')
    for aa in data_frame:
        test = aa[['PCBANK', 'PAYER', 'BCBANK', 'BENENAME']]
        for row in test.itertuples(index=False, name='new_test'):
            # print("开始时间")
            start_time = time.time()
            test1 = str(getattr(row, 'PCBANK')).strip()
            test2 = str(getattr(row, 'PAYER')).strip()
            test3 = str(getattr(row, 'BCBANK')).strip()
            test4 = str(getattr(row, 'BENENAME')).strip()
            # print(test1,test2)
            # print('放入队列')
            q.put("{0:s},{1:s},{2:s},{3:s}".format(test1, test2, test3, test4))
            # print(all_data)
            if q.qsize() == 10000:
                # print('队列大小为 10000，暂停')
                end_time = time.time()
                print("队列耗时 : {}".format(end_time - start_time))
                await my_test()
        if q.qsize() != 0:
            await my_test()


async def json_data():
    await take_data()
    # 对大队列进行统计，写入json文件中
    dict_all = {}
    for i in range(q_dict.qsize()):
        # print(q_dict.get())
        count_dict = dict(q_dict.get())
        dict_all = Counter(dict_all) + Counter(count_dict)
    # print(sum(dict(dict_all).values()))
    # print(dict(dict_all))
    with open('D:/data/cbcp_20191011/dict_all.txt', 'w', encoding='gb18030', newline='') as file:
        file.write(json.dumps(dict(dict_all), ensure_ascii=False))


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([json_data()]))
    loop.close()
    end_time = time.time()
    print("总耗时 : {}".format(end_time - start_time))
    # 总耗时: 419.4879639148712
    # dict_q = dict(Counter(list_q))
    # print(sum(dict_q.values()))
