#!/usr/bin/python3
# coding:utf-8
# 对大文件,根据 大小 进行切割，多线程处理分割后的文件，再清洗文件
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

file_path = 'D:/2000W/1-200W.csv'
out_path = 'D:/2000W/01'


def WirtFile(output_filename, list):
    with open(output_filename, 'w', encoding='gb18030', newline='') as write_file:
        # filewrite = csv.writer(csv_write_file)
        for row in list:
            write_file.write('{}\n'.format(row))
        # print(output_filename)


def CutFile(file_size, queue):
    with open(file_path, 'r', encoding='UTF-8', newline='') as file:
        # 定义空列表
        list_line = []
        # 定义计数，方便保存文件名
        file_name = 1
        # 逐行读取文件
        for line in file:
            line = line.strip()
            # 加入列
            list_line.append(line)
            # 判断列长度
            if len(list_line) == file_size * 1000:
                # 写入文件
                file_all_name = '{out_path}/{file_name}.csv'.format(out_path=out_path, file_name=file_name)
                # WirtFile(file_all_name,list_line)
                queue.put(file_all_name)
                file_name += 1
                # 清空列
                list_line = []
                continue
        # 剩下的部分直接写
        # WirtFile('{out_path}/{file_name}.csv'.format(out_path = out_path,file_name = '0'),list_line)
        queue.put('{out_path}/{file_name}.csv'.format(out_path=out_path, file_name='0'))


def chean_data(filename):
    time.sleep(0.5)
    return 1


# 通过共享变量(全局变量)，貌似方便些
def queue_list(queue):
    # 队列转换成列表
    file_list = []
    for i in range(queue.qsize()):
        # yield file_list.append(queue.get)
        file_list.append(queue.get())
    return file_list


if __name__ == "__main__":
    start_time = time.time()
    queue = Queue()
    theard_num = 20
    CutFile(10, queue)
    print("cut time is : {}".format(time.time() - start_time))
    # 建立线程池
    with ThreadPoolExecutor(theard_num) as executor:
        start_time = time.time()
        # 提交线程池
        # 问题，submit 是列表，持续增长的队列，如何搞？
        all_task = [executor.submit(chean_data, (file_name)) for file_name in queue_list(queue)]
        for future in as_completed(all_task):
            # 获得返回值
            data = future.result()
            # print("exe result : {}".format(data))
            # 计算线程池完成时间
        print("thread time is : {}".format(time.time() - start_time))
