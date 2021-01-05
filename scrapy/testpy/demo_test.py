#!/usr/bin/python
import sys,requests,time,hashlib,re
sys.path.append("..")
reload(sys)
from lxml import etree,html
from etc.setting_general import url,header
from etc.setting_mysql import * 
from lib.DBTool import  mysql


def get_href(url,ID):
    request_path = url + ID
    respone = requests.request('get',request_path,headers=header)
    tree = etree.HTML(respone.text)
    classname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[2]/text()')
    medthodname = tree.xpath('//body/*[@id="main-container"]/div[2]/div[2]/table/tr[2]/td[3]/text()')
    inurl = tree.xpath('//body/*[@id="main-container"]//a[contains(@onclick,"return show")]/@href') 
    pattern = re.compile('/')
    if re.findall(pattern,str(medthodname)):
#       print "==="
       sys.exit()
    #html.tostring(classname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(medthodname[0],encoding='utf-8').decode('utf-8')
    #html.tostring(inurl[0],encoding='utf-8').decode('utf-8')
    try:
        classname = classname[0].split('-')[1]
        medthodname = medthodname[0]
    except:
        classname = 'None'
        medthodname = 'None'

    if len(inurl) != 0:
        list_all.append('{}*{}_{}*{}'.format(ID,classname,medthodname,inurl))
        dict_all[ID]=('{}_{}'.format(classname,medthodname))
        for i in inurl:
            get_href(url,i.split('/')[-1])
    else:
        dict_all[ID]=('{}_{}'.format(classname,medthodname))

def insertdb(md5,long_list):
    mydb = mysql(apm_host,apm_port,amp_database,apm_user,apm_passwd)
    #sql = 'insert into result_scrapy(md5,long_list) values("{}","{}")'.format(md5,long_list)
    sql = 'insert into result_scrapy(md5,long_list) values ("{}","{}") on duplicate key update long_list="{}"'.format(md5,long_list,long_list)
    with mydb:
        rows = mydb.exec_sql(sql)
    #return rows

def md5(text):
    your_md5 = hashlib.md5(text).hexdigest()
    return your_md5
    
def main():
    try:
        bizTraceId = sys.argv[1]
    #except Exception as e:
        #print e
    except :
        print 'python {} {}'.format(sys.argv[0],'bizTraceId')
        sys.exit()
        
    global list_finall,list_all,dict_all
    list_finall = []
    list_all = []
    dict_all = {}
    get_href(url,bizTraceId)
    for i in list_all:
        key =  i.split('*')[1]
        list_value  =  i.split('*')[2]
        for k in eval(list_value):
            id_key = k.split('/')[-1]
            list_finall.append('{}*{}'.format(key,dict_all.get(id_key)))
    list_md5 = md5(str(list_finall))
    print list_md5
    print list_finall
    #print list(set(list_finall))
    #if len(list_finall) != 0:
    #    insertdb(list_md5,list(set(list_finall)))

if __name__ == '__main__':
    main()
