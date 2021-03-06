#!/usr/bin/python
import requests,json
from etc.setting_general import header,get_url,add_url,ship_url,add_count
from etc.setting_mysql import *
from lib.DBTool import  mysql


#mydb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
#sql = 'select md5,long_list from result_scrapy'
#with mydb:
#    rows = mydb.exec_sql(sql)


def insert_neo4j(md5,row):
#    md5 = i[0]
#    row = eval(row)
    request_url=get_url.format(md5)
    respone = requests.request('get',request_url,headers=header,timeout=10)
    result = json.loads(respone.text)
    myinfo='fbi'
    result = result['context']['serviceNodeList']
    if result:
        for i in result:     
            neo4j_ID = i['id']
            neo4j_count =  int(i['count']) + 1
            request_url_count = add_count.format(neo4j_ID,neo4j_count)
            print request_url_count
            respone = requests.request('get',request_url_count,headers=header,timeout=10)
            print respone.text
    
    else:
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
                    
if __name__ == '__main__':
    md5='923ff0451222c8c50f47393dc25953d6'
    row = ['com.czb.eatp.ast.api.AssetQueryService_queryMyAssetSummary*com.czb.eatp.user.api.UserEntInfoService_queryEntBasicInfo', 'com.czb.eatp.ast.api.AssetQueryService_queryMyAssetSummary*com.czb.afp.service.api.AssetQueryService_queryAssetListForOtherSystem', 'com.czb.eatp.ast.api.AssetQueryService_queryMyAssetSummary*com.czb.eatp.txn.api.AssetQueryService_queryMyAssetSummary', 'com.czb.eatp.user.api.UserEntInfoService_queryEntBasicInfo*com.czb.hades.esbout.api.CzbEsbService_doEsbCall']
    insert_neo4j(md5,row)

