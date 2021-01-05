#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,requests,time,hashlib,re,json
sys.path.append("..")
reload(sys)
from lxml import etree,html
from lib.logger import Log
from etc.setting_general import url, header,get_url,add_url,ship_url,add_count
from etc.setting_mysql import * 
from lib.DBTool import  mysql

log = Log.make_logger()

def get_href(url,ID):
    #pattern_ID = re.compile('default') 
    #if not re.findall(pattern_ID,ID):
    #    log.info("get---->{}".format(ID))
    request_path = url + ID
    chk_ID.append(ID)
    respone = requests.request('get',request_path,headers=header,timeout=10)
    tree = etree.HTML(respone.text)
    classname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[2]/text()')
    medthodname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[3]/text()')
    inurl = tree.xpath('//body/*[@id="main-container"]//a[contains(@onclick,"return show")]/@href') 
    pattern = re.compile('/')
    if re.findall(pattern,str(medthodname)):
        #log.info("not pattern -> {} <- exit".format(medthodname))
        sys.exit()
    #html.tostring(classname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(medthodname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(inurl[0],encoding='utf-8').decode('utf-8')
    else:
        try:
            classname = classname[0].split('-')[1]
        except:
            classname = classname[0]

        global n_order 
        n_order = n_order + 1
        medthodname = "{}${}".format(medthodname[0],n_order)

        if len(inurl) != 0:
            list_all.append('{}*{}_{}*{}'.format(ID,classname,medthodname,inurl))
            dict_all[ID]=('{}_{}'.format(classname,medthodname))
            for i in inurl:
                new_id = i.split('/')[-1]
                if new_id not in chk_ID:
                    get_href(url,new_id)
        else:
            dict_all[ID]=('{}_{}'.format(classname,medthodname))

#def insertdb(md5,long_list):
#    mydb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
#    #sql = 'insert into result_scrapy(md5,long_list) values("{}","{}")'.format(md5,long_list)
#    sql = 'insert into result_scrapy(md5,long_list) values ("{}","{}") on duplicate key update long_list="{}"'.format(md5,long_list,long_list)
#    log.info("insert ----> {}".format(md5))
#    with mydb:
#        rows = mydb.exec_sql(sql)
#    #return rows

def md5(text):
    #your_md5 = hashlib.md5(text).hexdigest()
    your_md5 = hashlib.sha256(text).hexdigest()
    return your_md5
    
def insert_neo4j(md5,dict_finall):
    request_url=get_url.format(md5)
    respone = requests.request('get',request_url,headers=header,timeout=10)
    result = json.loads(respone.text)
    myinfo='fbi'
    result = result['context']['serviceNodeList']
    if result:
        for i in result:     
            neo4j_ID = i['id']
            neo4j_count =  int(i['count']) + 1
            neo4j_todayCount =  int(i['todayCount']) + 1
            request_url_count = add_count.format(neo4j_ID,neo4j_count,neo4j_todayCount)
            log.info(request_url_count)
            respone = requests.request('get',request_url_count,headers=header,timeout=10)
            #log.info(respone.text)
            log.info(respone.status_code)
    
    else:
        for key,value in dict_finall.items():
            a,b = value.split('*')
    
            a_className = a.split('_')[0]
            a_methodName_order = a.split('_')[1:][0]
            a_methodName,a_order = a_methodName_order.split('$')
            b_className = b.split('_')[0]
            b_methodName_order = b.split('_')[1:][0]
            b_methodName,b_order = b_methodName_order.split('$')

            a_add_request_url = add_url.format(a_className,a_methodName,md5,a_order)
            b_add_request_url = add_url.format(b_className,b_methodName,md5,b_order)
            
            a_respone = requests.request('get',a_add_request_url,headers=header,timeout=10)
            a_result = json.loads(a_respone.text)
            a_id = a_result['context']['serviceNodeList'][0].get("id")
    
            b_respone = requests.request('get',b_add_request_url,headers=header,timeout=10)
            b_result = json.loads(b_respone.text)
            b_id = b_result['context']['serviceNodeList'][0].get("id")
    
            ship_url_ab = ship_url.format(a_id,b_id,key)
            log.info(ship_url_ab)
            ship_a_b = requests.request('get',ship_url_ab,headers=header,timeout=10)
            log.info(ship_a_b.text)
            #log.info(ship_a_b.status_code)

def clear_list(list_ojb):

    BC_list = []
    BC_dict = {}
    BC_num = 0

    dict_ojb = {}
    duble_list1 = []
    duble_list2 = []
    in_clear_list = []
    for i in list_ojb:
        BC_num = BC_num + 1
        ojb_A,ojb_B = i.split('*')
        ojb_A_name,ojb_A_order = ojb_A.split('$')
        ojb_B_name,ojb_B_order = ojb_B.split('$')
        duble_str = '{}{}'.format(ojb_A,ojb_B_name)
        if ojb_A_name != ojb_B_name :
            BC_dict[BC_num] = i
            BC_list.append(ojb_A)
            ojb_A_and_ojb_B = '{}*{}'.format(ojb_A_name,ojb_B_name)
            if ojb_A_and_ojb_B not in duble_list1:
                dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))
                duble_list1.append(ojb_A_and_ojb_B)
                duble_list2.append(duble_str)
            else:
                if duble_str not in duble_list2:
                    duble_list2.append(duble_str)
                    dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))
        else:
            in_clear_list.append('{}${}-{}${}'.format(ojb_A_name,ojb_A_order,ojb_B_name,ojb_B_order))
                
    BC_list = list(set(BC_list))
    for key,value in BC_dict.items():
        A,B = value.split('*')
        if B in BC_list:
            ojb_A, ojb_B = value.split('*')
            ojb_A_name, ojb_A_order = ojb_A.split('$')
            ojb_B_name, ojb_B_order = ojb_B.split('$')
            dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))

    new_dict_ojb = {v:k for k,v in dict_ojb.items()}
    finall_dict = {}
    num = 0
    for i in sorted(new_dict_ojb.keys()):
        num = num + 1
        finall_dict[num] = new_dict_ojb[i]

    for i in in_clear_list:
        A_target,B_target = i.split('-')
        str_dict = str(finall_dict).replace(A_target,B_target)

    return eval(str_dict)

def main():
    try:
        bizTraceId = sys.argv[1]
    #except Exception as e:
        #print e
    except :
        print 'python {} {}'.format(sys.argv[0],'bizTraceId')
        sys.exit()
        
    global list_finall,list_all,dict_all,chk_ID,n_order
    n_order = 0
    list_finall = []
    list_all = []
    dict_all = {}
    chk_ID =[]
    get_href(url,bizTraceId)
    for i in list_all:
        key =  i.split('*')[1]
        list_value  =  i.split('*')[2]
        for k in eval(list_value):
            id_key = k.split('/')[-1]
            list_finall.append('{}*{}'.format(key,dict_all.get(id_key)))


    dict_finall = clear_list(list_finall)

    if len(dict_finall) != 0:
        log.info('=========================================')
        log.info('get --> {} '.format(bizTraceId))
        log.info(list_finall)
        log.info(dict_finall)
        list_md5 = md5(str(dict_finall))
        log.info(list_md5) 
        log.info('-----------------------------------------')
        #insertdb(list_md5,list(set(list_finall)))
        insert_neo4j(list_md5,dict_finall)

if __name__ == '__main__':
    main()



