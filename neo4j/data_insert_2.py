#encoding:utf-8
#耗时 ： 476.36
import json
from py2neo import Graph,Node,NodeMatcher,Relationship,RelationshipMatcher
import asyncio
import time

file = 'D:/data/backup/dict_all.txt'
g = Graph("bolt://localhost:7687",user='neo4j',password='root123')
matcher = NodeMatcher(g)

async def bank_and_enterprise(bank,enterprise):
    print(bank,enterprise)
    matcher_bank = g.run("merge (a:master {name:'%s'}) return a.name" %(bank))
    print("创建master: {}".format(list(matcher_bank)))
    matcher_enterprise = g.run("merge (a:slave {name:'%s',type:'%s'}) return a.name" %(enterprise,bank))
    print("创建slave : {}".format(list(matcher_enterprise)))
    matcher_ship = g.run("match (a:master {name:'%s'}),(b:slave {name:'%s',type:'%s'}) "
                         "merge (a)-[r:拥有]->(b) return a.name,b.name"%(bank,enterprise,bank))
    print("创建ship : {}".format(list(matcher_ship)))

def enterprise_to_enterprise(bank1, en1, bank2, en2, times):
    create_ship=g.run("match (a:slave),(b:slave) where a.name='%s' and a.type='%s' and b.name='%s' and b.type='%s' "
          "create (a)-[r:过往 { 次数:%s }]->(b) return type(r) " % (en1, bank1, en2, bank2, times))
    print("过往ship : {}".format(list(create_ship)))


async def main():
    with open(file,'r',encoding='gb18030') as f:
        json_data = json.loads(f.read())
        # print(json_data)
        for key,values in json_data.items():
            # times = Relationship.type("{}".format(values))
            xx = key.split(",")
            pcbank = xx[0]
            payer = xx[1]
            bcbank = xx[2]
            benename = xx[3]
            if len(pcbank)&len(payer)&len(bcbank)&len(benename) != 0:
                await bank_and_enterprise(pcbank,payer)
                await bank_and_enterprise(bcbank,benename)
                enterprise_to_enterprise(pcbank,payer,bcbank,benename,values)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main()]))
    loop.close()
    end_time = time.time()
    print("时间:{:.2f}".format(end_time - start_time))
    # main()