#!/usr/bin/python
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
    log.info("get---->{}".format(ID))
    request_path = url + ID
    chk_ID.append(ID)
    respone = requests.request('get',request_path,headers=header,timeout=10)
    tree = etree.HTML(respone.text)
    classname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[2]/text()')
    medthodname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[3]/text()')
    inurl = tree.xpath('//body/*[@id="main-container"]//a[contains(@onclick,"return show")]/@href') 
    pattern = re.compile('/')
    if re.findall(pattern,str(medthodname)):
        log.info("not pattern -> {} <- exit".format(medthodname))
        sys.exit()
    #html.tostring(classname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(medthodname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(inurl[0],encoding='utf-8').decode('utf-8')
    global n_order 
    #try:
    #    classname = classname[0].split('-')[1]
    #    medthodname = medthodname[0]
    #except:
    n_order = n_order + 1
    classname = classname[0]

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
    
def insert_neo4j(md5,row):
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
        for j in row:
            a,b = j.split('*')
            if a != b:
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
    
                ship_url_ab = ship_url.format(a_id,b_id)
                log.info(ship_url_ab)
                ship_a_b = requests.request('get',ship_url_ab,headers=header,timeout=10)
                #log.info(ship_a_b.text)
                log.info(ship_a_b.status_code)
            else:
                log.info("{} === {} same exit ".format(a,b))
def main():
    try:
        bizTraceId = sys.argv[1]
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
    log.info(list_all)
    for i in list_all:
        key =  i.split('*')[1]
        list_value  =  i.split('*')[2]
        for k in eval(list_value):
            id_key = k.split('/')[-1]
            list_finall.append('{}*{}'.format(key,dict_all.get(id_key)))
    list_md5 = md5(str(set(list_finall)))
    log.info(list_finall)
    if len(list_finall) != 0:
        #insertdb(list_md5,list(set(list_finall)))
        insert_neo4j(list_md5,list(set(list_finall)))

if __name__ == '__main__':
    main()
