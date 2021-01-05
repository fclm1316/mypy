#!/usr/bin/python
url = 'http://192.3.237.208:8080/cat/r/m/'
#ip = '192.3.250.116'
ip = '192.3.250.130'
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
       }
get_url ='''http://''' + ip + ''':9080/neo-restful-version-1/ServiceNode/getServiceNodeList?mode=4&md5={}'''
add_url ='''http://''' + ip + ''':9080/neo-restful-version-1/ServiceNode/addServiceNodeList?className={}&methodName={}&md5={}&order={}'''
ship_url ='''http://''' + ip + ''':9080/neo-restful-version-1/CallLinkRelationship/add?startNodeId={}&endNodeId={}&realationOrder={}'''
add_count = '''http://''' + ip + ''':9080/neo-restful-version-1/ServiceNode/modifyServiceNodeList?id={}&count={}&todayCount={}'''
