#!/usr/bin/python
import requests,json
from etc.setting_general import header,get_url,add_url,ship_url
from etc.setting_mysql import *
from lib.DBTool import  mysql


#request_url=get_url.format(md5)
#respone = requests.request('get',request_url,headers=header)
#result = json.loads(respone.text)
#print result['context']['serviceNodeList']
mydb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
sql = 'select md5,long_list from result_scrapy'
with mydb:
    rows = mydb.exec_sql(sql)

for i in rows:
    md5 = i[0]
    row = eval(i[1])
    request_url=get_url.format(md5)
    respone = requests.request('get',request_url,headers=header)
    result = json.loads(respone.text)
    myinfo='fbi'
    if not result['context']['serviceNodeList']:
        for j in row:
            a,b = j.split('*')
            if a != b:
                #print a.split('_')[0],a.split('_')[1],b.split('_')[0],b.split('_')[0]
                #a_className , a_methodName = a.split('_')
                a_className = a.split('_')[0]
                a_methodName = a.split('_')[1:][0]
                b_className , b_methodName = b.split('_')
                a_add_request_url = add_url.format(a_className,a_methodName,md5,myinfo)
                b_add_request_url = add_url.format(b_className,b_methodName,md5,myinfo)

                a_respone = requests.request('get',a_add_request_url,headers=header)
                #print a_add_request_url
                #print a_respone.status_code
                a_result = json.loads(a_respone.text)
                a_id = a_result['context']['serviceNodeList'][0].get("id")

                b_respone = requests.request('get',b_add_request_url,headers=header)
                b_result = json.loads(b_respone.text)
                b_id = b_result['context']['serviceNodeList'][0].get("id")

                ship_url_ab = ship_url.format(a_id,b_id)
                print ship_url_ab
                ship_a_b = requests.request('get',ship_url_ab,headers=header)
                print ship_a_b.text
                
