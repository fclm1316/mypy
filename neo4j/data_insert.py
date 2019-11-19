#encoding:utf-8
# 代码太慢
import json
from py2neo import Graph,Node,NodeMatcher,Relationship,RelationshipMatcher
import asyncio


file = 'D:/data/backup/dict_all.txt'
g = Graph("bolt://localhost:7687",user='neo4j',password='root123')
matcher = NodeMatcher(g)

async def bank_and_enterprise(bank,enterprise):
    node_bank = Node("bank", name="{}".format(bank))
    print(bank,enterprise)
    node_enterprise = Node("enterprise", name="{}".format(enterprise),type="{}".format(bank))
    matcher_bank = g.run("match (a:bank) where a.name='{0:s}' return a.name".format(bank))
    # print('查询bank{}'.format(list(matcher_bank)))
    matcher_enterprise = matcher.match("enterprise").where("_.name='{}'".format(enterprise),"_.type='{}'".format(bank))
    # print(matcher_enterprise)
    if len(list(matcher_bank)) == 0:
        print('创建bank:{} '.format(bank))
        g.create(node_bank)
    if len(list(matcher_enterprise)) == 0:
        print('创建enterprise:{}'.format(enterprise))
        g.create(node_enterprise)
    matcher_ship = g.run("match (a:bank)-[r:拥有]->(b:enterprise) where a.name='{0:s}' and b.name='{1:s}' and b.type='{2:s}' "
                         "return type(r)"
                         .format(bank,enterprise,bank))
    if len(list(matcher_ship)) == 0:
        print('创建ship')
        g.run("match (a:bank),(b:enterprise) where a.name='{0:s}' and b.name='{1:s}' and b.type='{2:s}' "
              "create (a)-[r:拥有]->(b) return type(r) "
                .format(bank, enterprise, bank))

async def enterprise_to_enterprise(bank1,en1,bank2,en2,times):
    g.run("match (a:enterprise),(b:enterprise) where a.name='%s' and a.type='%s' and b.name='%s' and b.type='%s' "
              "create (a)-[r:过往 { 次数:%s }]->(b) return type(r) " %(en1,bank1,en2,bank2,times))
    print("过往")


    # matcher_enterprise = matcher.match("enterprise").where("_.name='{}'".format(enterprise))
    # matcher_bank_enterprise = g.run(
    #     "match (a:bank)-[r:拥有]->(b:enterprise) where a.name ='{0:s}' "
    #     "and b.name='{1:s}' and b.type='{2:s}' return type(r)".format(bank,enterprise,bank))
    # if len(list(matcher_bank_enterprise)) == 0:
    #     g.create(node_enterprise)
    #     g.run("match (a:bank),(b:enterprise) where a.name='{0:s}' and b.name='{1:s}' and b.tpye={2:s} "
    #           "create (a)-[r:拥有]->(b) return type(r) ".format(bank, enterprise,bank))


# def bank_and_enterprise(bank1, enterprise1,bank2,enterprise2,knows):
    # print(bank1)
    # matcher_bank1= g.run("match (a:bank) where a.name='{0:s}'  return a.name".format(bank1))
    # matcher_bank1 = matcher.match("bank").where("_.name='{}'".format(bank1))
    # matcher_enterprise1 = matcher.match("enterprise").where("_.name='{}'".format(enterprise1))
    # node_bank = Node("bank", name="{}".format(bank1))
    # node_enterprise = Node("enterprise", name="{}".format(enterprise1))
    # print(list(matcher_bank1))
    # if  len(list(matcher_bank1)) == 0:
    #     g.create(node_bank)
        # print("aa")
        # g.create(node_enterprise)
        # ship = Relationship(node_bank,"拥有",node_enterprise)
        # g.create(ship)
    # else:
    #     g.create(node_bank)
    # matcher_enterpprise1 = g.run("Match (a:bank)-[:拥有]-(b:enterprise) where a.name='{0:s}' and b.name='{1:s}' return b.name".format(bank1,enterprise1))
    # print(list(matcher_enterpprise))
    # if len(list(matcher_enterpprise1)) == 0:
    #     g.create(node_enterprise)
    # ship = Relationship(node_bank,"拥有",node_enterprise)
    # g.create(ship)
        # print("aa")

    # matcher_bank2 = matcher.match("bank").where("_.name='{}'".format(bank2))
    # if not matcher_bank2:
    #     node_bank = Node("bank",name="{}".format(bank2))
    #     g.create(node_bank)
    #     node_enterprise = Node("enterprise",name="{}".format(enterprise2))
    #     g.create(node_enterprise)
    #     ship = Relationship(matcher_bank2,"拥有",node_enterprise)
    #     g.create(ship)

# matcher = NodeMatcher(g)
# matcher_pcbank = matcher.match("{}".format(bank)).where("_.name='{}'".format(pcbank))
# matcher_bckank = matcher.match("{}".format(bank)).where("_.name='{}'".format(bcbank))
# matcher_palyer = matcher.match("{}".format(enterprise)).where("_.name='{}'".format(payer))
# matcher_benename = matcher.match("{}".format(enterprise)).where("_.name='{}'".format(benename))
# matcher = NodeMatcher(g)
# if matcher.match("".format(type)).where("_.name='{}'".format(name)):
    #     pass
    # else:
    #     pass

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
                await enterprise_to_enterprise(pcbank,payer,bcbank,benename,values)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([main()]))
    loop.close()

    # main()