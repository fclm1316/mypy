#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,requests,time,re,json
from lib.logger import Log
from setting_mysql import neo4j_esb_config
from MysqlTools import mydb
now = time.time()
timeArray = time.localtime(now)
timeFormat = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
ip='203.3.250.116'
business_add_url = "http://"+ip+":9080/neo-restful-version-1/Business/add"
interface_base_url = "http://"+ip+":9080/neo-restful-version-1/ServiceNode/addServiceNodeList"
system_base_url =  "http://"+ip+":9080//neo-restful-version-1/SystemNode/addSystemNodeList"
invoke_base_url =  "http://"+ip+":9080//neo-restful-version-1/InvokeRelationship/add"
provide_base_url =  "http://"+ip+":9080//neo-restful-version-1/ProvideRelationship/add"
effect_base_url= "http://"+ip+":9080//neo-restful-version-1/EffectRelationship/add"
business_sql = """
SELECT
    `mastran_code` AS '业务代码',
    `mastrancode_ch` AS '业务名称',
    `requester` AS '请求方编号',
    `requester_ch` '请求方中文'
FROM
    `neo4j`.`esb_operation_service`
GROUP BY
    `mastran_code`,
    `mastrancode_ch`,
    `requester`,
    `requester_ch`
"""
interface_sql = """
SELECT
  `interface_en` AS '服务接口名称',
  `operation_en` AS '服务操作名称',
  `interface_ch` AS '接口中文名称',
  `operation_ch` AS '服务中文名称',
  `provider`    AS '提供方ID'   ,
  `provider_ch` AS '服务提供方系统中文名称',
  `cbs_operation_id` AS '核心服务ID',
  `cbs_operation_name` AS '核心后台服务名称',
  `cbs_operation_describle` AS '核心服务描述'

FROM
  `neo4j`.`esb_operation_service`
GROUP BY
    interface_en,operation_en,provider,interface_ch,operation_ch,provider_ch,cbs_operation_id,cbs_operation_name,cbs_operation_describle


"""
system_request_sql = "SELECT `requester` AS '请求方编号',`requester_ch` '请求方中文' FROM `neo4j`.`esb_operation_service` GROUP BY `requester`,`requester_ch`"
system_provider_sql = "SELECT `provider` AS '提供方ID',`provider_ch` AS '服务提供方系统中文名称' FROM `neo4j`.`esb_operation_service` GROUP BY provider,provider_ch"
effect_sql = """
SELECT
    `requester` AS '请求方编号',
    `requester_ch` '请求方中文',
    `interface_en` AS '服务接口名称',
    `interface_ch` AS '接口中文名称',
    `operation_en` AS '服务操作名称',
    `operation_ch` AS '服务中文名称',
    `provider` AS '提供方ID',
    `provider_ch` AS '服务提供方系统中文名称',
    `mastran_code` AS '业务代码',
    `mastrancode_ch` AS '业务名称',
    `cbs_operation_id` AS '核心服务ID',
    `cbs_operation_name` AS '核心后台服务名称',
    `cbs_operation_describle` AS '核心服务描述',
    `times` AS '调用频次',
    `importance` AS '重要性'
FROM
    `neo4j`.`esb_operation_service`
"""

system_cql = """{
                'systemESBID':'%(systemESBID)s',
                'systemName':'%(systemName)s',
                'insertTime':'%(insertTime)s',
                'insertOperationStaff':'System',
                'modifyTime':' ',
                'modifyOperationStaff':' '
            }"""

interface_cql = """{ 'interfacename':'%(interfacename)s','operationname':'%(operationname)s','ch_interfacename':'%(ch_interfacename)s','ch_operationname':'%(ch_operationname)s','provider':'%(provider)s','ch_provider':'%(ch_provider)s','cbs_fwid':'%(cbs_fwid)s','cbs_htfwmc':'%(cbs_htfwmc)s','cbs_fwms':'%(cbs_fwms)s','info':'备注预留字段','insertTime':'%(insertTime)s','insertOperationStaff':'System','modifyTime':'','modifyOperationStaff':''}"""
business_cql = """{
            "businessCode":"%(businessCode)s",
            "businessCodeChineseName":"%(businessCodeChineseName)s",
            "businessInfo":"",
            "backupInfo":"",
            "systemESBID":"%(systemESBID)s",
            "systemName":"%(systemName)s",
            "insertOperationStaff":"",
            "insertTime":"%(insertTime)s",
            "modifyOperationStaff":"",
            "modifyTime":""
           }"""
realationship_Cql = """
{'startNodeId':'%(startNodeId)s','endNodeId':'%(endNodeId)s','insertTime':'%(insertTime)s','insertOperationStaff':'System','modifyTime':' ','modifyOperationStaff':' '}
"""
effect_Cql = """
{'startNodeId':'%(startNodeId)s','endNodeId':'%(endNodeId)s','insertTime':'%(insertTime)s','insertOperationStaff':'System','modifyTime':' ','modifyOperationStaff':' ','times':'%(times)d','importance':'%(importance)d'}
"""


def add_business(result):
    for j in result:
        i = list(j)
        businessCode = i[0]
        businessCodeChineseName = i[1]
        systemESBID = i[2]
        systemName = i[3]
        business_dic1 = business_cql % dict(businessCode=businessCode, businessCodeChineseName=businessCodeChineseName,
                                            systemESBID=systemESBID, systemName=systemName, insertTime=timeFormat)

        #dic2 = eval(business_dic1)
        parms_value=eval(business_dic1)
        print(parms_value)
	    r=requests.request('get',business_add_url,params=parms_value,headers=header,timeout=10)
        print(r.url)
        #response = req.read().decode()
        # print(response)
        #rebusinessDict(response, businessCode, systemESBID)


def addsystem(result):
    for j in result:
        i = list(j)
        systemESBID = i[0]
        systemName = i[1]
        system_dic1 = system_cql % dict(systemESBID=systemESBID, systemName=systemName, insertTime=timeFormat)
        dic2 = eval(system_dic1)
        data = parse.urlencode(dic2, encoding="utf-8")
        # print(base_url+'%s'%data)
	system_base_url=system_base_url + '%s' % data
	req=requests.request('get',system_base_url,headers=header,timeout=10)
        #req = request.urlopen(system_base_url + '%s' % data)
        response = req.read().decode()
        resystemDict(response, systemESBID, systemName)
def add_interface(result):
    for j in result:
        i = list(j)
        interfacename = i[0]
        operationname = i[1]
        ch_interfacename = i[2]
        ch_operationname = i[3]
        provider = i[4]
        ch_provider = i[5]
        cbs_fwid = i[6]
        cbs_htfwmc = i[7]
        cbs_fwms = i[8]
        interface_dic1 = interface_cql % dict(interfacename=interfacename, operationname=operationname,
                                              ch_interfacename=ch_interfacename, ch_operationname=ch_operationname,
                                              provider=provider, ch_provider=ch_provider, cbs_fwid=cbs_fwid,
                                              cbs_htfwmc=cbs_htfwmc, cbs_fwms=cbs_fwms, insertTime=timeFormat)
        dic2 = eval(interface_dic1)
        data = parse.urlencode(dic2, encoding="utf-8")
        # print(base_url + '%s' % data)
        #req = request.urlopen(interface_base_url + '%s' % data)
        # print(req.read().decode())
        response = req.read().decode()
        reinterfaceDict(response, interfacename, operationname, provider)


def reinterfaceDict(response, interfacename, operationname, provider):
    dict_value = re.findall(r"\"id\":(.*?),", response).pop(0)
    dict_key = '{}{}{}'.format(interfacename, operationname, provider)
    dict_interface[dict_key] = dict_value
    # print(dict_interface)


def resystemDict(response, aa, bb):
    dict_value = re.findall(r"\"id\":(.*?),", response).pop(0)
    dict_key = '{}{}'.format(aa, bb)
    dict_system[dict_key] = dict_value
    # print(dict_system)


def rebusinessDict(response, businessCode, systemESBID):
    dict_value = re.findall(r"\"id\":(.*?),", response).pop(0)
    dict_key = '{}{}'.format(businessCode, systemESBID)
    dict_business[dict_key] = dict_value


def addrealationship(result):
    for j in result:
        i = list(j)
        systemESBID = i[0]
        systemName = i[1]
        interfacename = i[2]
        operationname = i[4]
        provider = i[6]
        ch_provider = i[7]
        businessCode = i[8]
        times = int(str(i[13]).replace('None', '0'))
        importance =int(str(i[14]).replace('None', '0'))
        system = "{}{}".format(systemESBID, systemName)
        system2 = "{}{}".format(provider, ch_provider)
        interface = "{}{}{}".format(interfacename, operationname, provider)
        business = "{}{}".format(businessCode, systemESBID)
        systemid = dict_system.get(system)
        providerid = dict_system.get(system2)
        interfaceid = dict_interface.get(interface)
        businessid = dict_business.get(business)
        if systemid != 'None' and interfaceid != 'None':
            invoke = realationship_Cql % dict(startNodeId=systemid, endNodeId=interfaceid, insertTime=timeFormat)
            invoke_dic = eval(invoke)
            data_invoke = parse.urlencode(invoke_dic, encoding="utf-8")
            # print(invoke_base_url + '%s' % data_invoke)
            req_invoke = request.urlopen(invoke_base_url + '%s' % data_invoke)
            print(req_invoke.read().decode())
        if providerid == 'None' and interfaceid == 'None':
            pass
        else:
            provider = realationship_Cql % dict(startNodeId=providerid, endNodeId=interfaceid, insertTime=timeFormat)
            provider_dic = eval(provider)
            data_provider = parse.urlencode(provider_dic, encoding="utf-8")
            # print(provide_base_url + '%s' % data_provider)
            req_provider = request.urlopen(provide_base_url + '%s' % data_provider)
            print(req_provider.read().decode())
        if businessid == 'None' and interfaceid == 'None':
            pass
        else:
            effect = effect_Cql % dict(startNodeId=interfaceid, endNodeId=businessid, insertTime=timeFormat,
                                       times=times, importance=importance)
            effect_dic = eval(effect)
            data_effect = parse.urlencode(effect_dic, encoding="utf-8")
            req_effect = request.urlopen(effect_base_url + '%s' % data_effect)
            print(req_effect.read().decode())


if __name__ == '__main__':
    dict_business = {}
    dict_interface = {}
    dict_system = {}
    db = mydb(neo4j_esb_config)
    with db:
        # result=db.exec_sql(sql)
        business_sql = db.exec_sql(business_sql)
        #interface_sql = db.exec_sql(interface_sql)
        #system_request_sql = db.exec_sql(system_request_sql)
        #system_provider_sql = db.exec_sql(system_provider_sql)
        #effect_sql = db.exec_sql(effect_sql)
    add_business(business_sql)
    #addsystem(system_request_sql)
    #addsystem(system_provider_sql)
    #add_interface(interface_sql)
    #addrealationship(effect_sql)
