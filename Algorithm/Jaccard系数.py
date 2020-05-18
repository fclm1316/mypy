#!/usr/bin/env python3
#encoding:utf-8
#使用Jaccard系数,找出sql相似度
#get_sql
#
import re
from mylib import MysqlTools:
from mylib.setting_mysql import apmdb

sel = 'select stmt_text,sql_md5 from oracle_slow_sql'
sql_text = ''

with get_data:
    sql_text = get_data.exec_sql(sql)

def To_list(str):
    new_list = []
    for i in str.split():
        new_list.append(i)
    return new_list
pattern1="select|update|\(|\)|as|where|and|join|=|like|\?|count|in|from|\'|,"
pattern2=",|\'|\(|\)|\*"
pattern3="update |delete |insert into|select | count| from | N | S | = | != | where | and | like | in | order by|" \
         "group by| desc | limit "
len_sql = len(sql_text)
for i in range(len_sql):
    next_one = i + 1
    text1 = re.sub(pattern2,' ',sql_text[i][0],flags=re.IGNORECASE)
    text1 = re.sub(pattern3,' ',text1,flags=re.IGNORECASE)
    text1_md5 = sql_text[i][1]
    list_text1 = To_list(text1)
    list_text1 = set(list_text1)
    for j in range(next_one,len_sql):
        text2 = re.sub(pattern2, ' ', sql_text[j][0],flags=re.IGNORECASE)
        text2 = re.sub(pattern3, ' ',text2,flags=re.IGNORECASE)
        text2_md5 = sql_text[j][1]
        list_text2 = To_list(text2)
        list_text2 = set(list_text2)

        temp = 0
        for c in list_text1:
            if c in list_text2:
                temp += 1
        fenmu = len(list_text1) + len(list_text2) - temp
        jaccard_conefficient = float(temp/fenmu)
        if jaccard_conefficient >0.7:
            print("{:.2f},{},{}".format(jaccard_conefficient,text1_md5,text2_md5))

