#!/usr/bin/env python3
#encoding:utf-8
#使用Jaccard系数,找出sql相似度
#get_sql
import threading
from queue import Queue,Empty
import re,pymysql,time
handsomedb ={
    'host':'127.0.0.1',
    'port':3306,
    'database':'handsomedb',
    'user':'handsome',
    'password':'Handsome@123'
}
sql_one = 'select stmt_text,sql_md5 from oracle_slow_sql where jaccard=2 limit 1;'
sql_all = 'select stmt_text,sql_md5 from oracle_slow_sql where jaccard is null;'
sql_object= ''
sql_taget=''
pattern2 = ",|\(|\)|=|\d+|\'(.*?)\'|\+|\/|>|<|#|;|%|\?|\||\/\*(.*?)\/\*"
pattern3 = "update |delete |insert into|select | count| from | where | and | like | in |order by|group by|" \
           " desc | limit | or | not | as | is | null | destinct | left | join | set"


def To_list(str):
    new_list = []
    text_taget = re.sub(pattern2," ",str,flags=re.IGNORECASE)
    text_taget = re.sub(pattern3," ",str,flags=re.IGNORECASE)
    for i in text_taget.split():
        new_list.append(i)
    return list(set(new_list))

def jaccard(taget_list,object_list):
    temp = 0
    # taget_list = set(taget_list)
    # object_list = set(object_list)
    for i in taget_list:
        if i in object_list:
            temp += 1
    fenmu = len(taget_list) + len(object_list) - temp
    return float(temp / fenmu)

def update_sql(table_name,jaccard,lineage,md5):
    sql='update {} set jaccard={},lineage="{}" where sql_md5="{}"'.format(table_name,jaccard,lineage,md5)
    return sql

def produce_data(q_produce,q_coustmer):
    conn = pymysql.connect(**handsomedb)
    all_cursor = conn.cursor()
    all_cursor.execute(sql_all)
    all_data = all_cursor.fetchall()
    if len(all_data) != 0:
        for sql,md5 in all_data:
            list_sql = To_list(sql)
            q_produce.put(list_sql)
            q_produce.put(md5)
            while q_produce.qsize() != 0:
                taget_sql = q_produce.get()
                taget_sql_md5 = q_produce.get()
                sql_update_self = update_sql('oracle_slow_sql',1,taget_sql_md5,taget_sql_md5)
                q_coustmer.put(sql_update_self)
                for i in range(q_produce.qsize()):
                    object_sql = q_produce.get()
                    object_sql_md5 = q_produce.get()
                    jaccard_coefficient = jaccard(taget_sql,object_sql)
                    if jaccard_coefficient >0.6:
                        sql_update_obj = update_sql('oracle_slow_sql',jaccard_coefficient,taget_sql_md5,object_sql_md5)
                        q_coustmer.put(sql_update_obj)
                    else:
                        q_produce.put(object_sql)
                        q_produce.put(object_sql_md5)
                global my_flag
                my_flag = 1
    conn.commit()
    all_cursor.close()
    conn.close()

# def coustmer_data(q_coustmer):
#     conn = pymysql.connect(**handsomedb)
#     update_cursor = conn.cursor()
#     while True:
#         global my_flag
#         if my_flag > 1:
#             try:
#                 sql = q_coustmer.get(timeout=2)
#                 print(sql)
#                 update_cursor.execute(sql)
#                 conn.commit()
#             except Empty:
#                 print("done")
#                 conn.commit()
#                 update_cursor.close()
#                 conn.close()
#                 break


def coustmer_data(q_coustmer):
    while True:
        global my_flag
        if my_flag > 0:
            with open('a.txt','w') as f:
                try:
                    sql = q_coustmer.get(timeout=2)
                    f.writelines('{}\n'.format(sql))
                    print(sql)
                except Empty:
                    print("done")
                    break


if __name__ == '__main__':
    start_time = time.time()
    global my_flag
    my_flag = 0
    q = Queue()
    q_coustmer = Queue()
    thead1 = threading.Thread(target=produce_data,args=(q,q_coustmer))
    thead2 = threading.Thread(target=coustmer_data, args=(q_coustmer,))
    thead1.start()
    thead2.start()
    thead1.join()
    thead2.join()

    print("-----------------------")
    print("time is : {:.2f}".format(time.time() - start_time))
    print("-----------------------")
