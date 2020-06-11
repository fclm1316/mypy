#!/usr/bin/env python3
# encoding:utf-8
# 使用Jaccard系数,找出sql相似度
# get_sql
#
import re, pymysql, time

handsomedb = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'handsomedb',
    'user': 'handsome',
    'password': 'Handsome@123'
}
sql_one = 'select stmt_text,sql_md5 from oracle_slow_sql where jaccard=2 limit 1;'
sql_all = 'select stmt_text,sql_md5 from oracle_slow_sql where jaccard=2 ;'
sql_object = ''
sql_taget = ''
pattern2 = ",|\(|\)|=|\d+|\'(.*?)\'|\+|\/|>|<|#|;|%|\?|\||\/\*(.*?)\/\*"
pattern3 = "update |delete |insert into|select | count| from | where | and | like | in |order by|group by|" \
           " desc | limit | or | not | as | is | null | destinct | left | join | set"


def To_list(str):
    new_list = []
    text_taget = re.sub(pattern2, " ", str, flags=re.IGNORECASE)
    text_taget = re.sub(pattern3, " ", str, flags=re.IGNORECASE)
    for i in text_taget.split():
        new_list.append(i)
    return new_list


def jaccard(taget_list, object_list):
    temp = 0
    taget_list = set(taget_list)
    object_list = set(object_list)
    for i in taget_list:
        if i in object_list:
            temp += 1
    fenmu = len(taget_list) + len(object_list) - temp
    return float(temp / fenmu)


conn = pymysql.connect(**handsomedb)
start_time = time.time()

while True:
    taget_cursor = conn.cursor()
    # 流式游标
    # object_cursor = conn.cursor(pymysql.cursors.SSCursor)
    object_cursor = conn.cursor()
    taget_cursor.execute(sql_one)
    object_cursor.execute(sql_all)
    sql_taget = taget_cursor.fetchall()
    sql_object = object_cursor.fetchall()
    if len(sql_taget) != 0:
        for taget_str, taget_sql_md5 in sql_taget:
            taget_list = To_list(taget_str)
            for object_str, object_sql_md5 in sql_object:
                object_list = To_list(object_str)
                jaccard_confficient = jaccard(taget_list, object_list)
                if jaccard_confficient > 0.4:
                    sql = 'update oracle_slow_sql set jaccard = {},lineage = "{}" where sql_md5 = "{}"'.format(
                        jaccard_confficient, taget_sql_md5, object_sql_md5)
                    print(sql)
                    update_cursor = conn.cursor()
                    update_cursor.execute(sql)
                    conn.commit()
                    update_cursor.close()
        taget_cursor.close()
        object_cursor.close()
    else:
        taget_cursor.close()
        object_cursor.close()
        conn.close()
        print("------------------")
        print("time is : {:.2f}".format(time.time() - start_time))
        print("------------------")
        break
