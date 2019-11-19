#encoding:utf-8
import pandas as pd
import pandas as pd
# file1 = 'D:/data/cbcp_20191011/newtest.txt'
# file2 = 'D:/data/cbcp_20191011/test.txt'
# file3 = 'D:/data/cbcp_20191011/dict_all.txt'
import json

# with open(file1,'a+',encoding='utf-8',newline="") as write_file:
#     with open(file2,'r',encoding='utf-8',newline="") as read_file:
#         write_file.write('\n')
        # for aa in read_file.readlines() :
        #     write_file.write(aa)


# data_frame = pd.read_csv(file2, encoding='utf-8', low_memory=False, chunksize=1000, delimiter="|")
# for aa in data_frame:
#     print(aa)
# with open(file2,'r',encoding='utf-8',newline="",) as read_file:
    # read_lines = read_file.readlines()
    # num = 0
    # for aa in read_file:
    #     num += 1
    #     if num == 2642460:
    #         print(len(aa.split("^")))
    #         print(aa)
    #     elif num == 2642461:
    #         print(len(aa.split("^")))
    #         print(aa)
    #     elif num == 2642462:
    #         print(len(aa.split("^")))
    #         print(aa)

        # if (len(aa.split('^'))) != 56:
        #     print(aa)
# with open(file3,'r',encoding='gb18030') as f:
#     json_data = json.loads(f.read())
#     print(json_data)
    # for key,values in json_data.items():
    #     print(key)
from py2neo import Graph,Node,Relationship,NodeMatcher,RelationshipMatcher

g = Graph("bolt://localhost:7687",user='neo4j',password='root123')

# test_node_1 = Node("Person",name = "test_name_1",type="bank")
# test_node_2 = Node("Person",name = "test_name_2",type="bank")
# test_node_3 = Node("Bank",name = "test_name_3")
# test_node_4 = Node("Bank",name = "test_name_4")
# noed_know1 = Relationship(test_node_1,"单项",test_node_2,times=10)
# noed_know2 = Relationship(test_node_3,"{0:s},{1:d}".format("单项",10 ),test_node_4)
# noed_know3 = Relationship(test_node_3,"单项",test_node_1,times=22)
# noed_know4 = Relationship(test_node_4,"单项",test_node_1,times=88)
# ship = Relationship.type("{}".format("单项"))
# noed_know2 = Relationship(test_node_3,"单项",test_node_4)
# noed_know3 = Relationship(test_node_3,"单项",test_node_1)
# noed_know4 = Relationship(test_node_4,"单项",test_node_1)
# noed_know5 = Relationship(test_node_1,"单项",test_node_4,times=30)
# noed_know6 = Relationship(test_node_1,"单项",test_node_2,times=109)
# g.create(test_node_1)
# g.create(test_node_2)
# g.create(test_node_3)
# g.create(test_node_4)
# g.create(noed_know1(test_node_2,test_node_3))
# g.merge(ship(test_node_1,test_node_2))
# g.merge(ship(test_node_1,test_node_3))
# g.merge(ship(test_node_1,test_node_4))
# g.merge(ship(test_node_2,test_node_3))
# g.delete(test_node_3)
g.delete_all()
# matcher = NodeMatcher(g)
# print(list(matcher.match("{0:s}".format("Person"),name="{0:s}".format("test_node_1"))))
# print(list(matcher.match("Person").where("_.name=~'te.*'").order_by("_.name").limit(3)))
#
# if matcher.match("{0:s}".format("Person"),name="{0:s}".format("test_node_6")):
#    print("haha")
# else:
#    print("KUKU")



# file = 'D:/data/cbcp_20191011/dict_all.txt'
# with open(file,'r',encoding='gb18030') as f:
#     json_data = json.loads(f.read())
#     print(json_data)
    # for key,values in json_data.items():
    #     node_know = Relationship.type("{}".format(values))
    #     xx = key.split(",")
    #     pcbank = xx[0]
    #     palyer = xx[1]
    #     bcbank = xx[2]
    #     benename = xx[3]
        # aa = key.split(",")[0]
        # bb = key.split(",")[1]
        # cc = key.split(",")[2]
        # dd = key.split(",")[3]

# a = g.run("Match (a:Person)-[:单项]-(b:Bank) where a.name='test_node_1' and b.name='test_node_3' return b.name")
# a = g.run("Match (a:Person)-[:单项]-(b:Bank) where a.name='{0:s}' and b.name='test_node_3' return b.name".format("test_node_1"))
#
# print(list(a))

# a = g.run("match (a:Person),(b:Bank) where a.name='test_name_1' and b.name='test_name_3' "
#           "create (a)-[r:拥有]->(b) return type(r)")
# a = g.run("match (a:Person),(b:Bank) where a.name='test_node_1' and b.name='test_node_3' return a")
# a = g.run("match (a {name:{0:s}})-[r:拥有]->(b {name:{1:s}}) return type(r)".format('test_name_1','test_name_2'))
# a = g.run("match (a {name:'test_name_1'})-[r:拥有]->(b {name:'test_name_3'}) return a.name")
# a = g.run("match (a:Person)-[r:拥有]->(b:Bank) where a.name='test_name_1' and b.name='test_name_3' return a.name")
# print(list(a))
# matcher_bank = g.run("match (a:bank) where a.name='{0:s}' return a".format('105851000019'))
# matcher_bank = g.run("match (a:bank) where a.name='%s' return a.name" % (num))
# matcher_bank=g.run("match (a:bank),(b:bank) where a.name='%s' and b.name='%s' "
#       "create (a)-[r:拥有 { 次数:%s}]->(b) return type(r) " % (num1,num2,num3))
# print(list(matcher_bank))
# a=g.run("match (a:enterprise),(b:enterprise) where a.name='%s' and a.type='%s' "
#         "and b.name='%s' and b.type='%s' "
#        "create (a)-[r:往来 { 次数:%s }]-20>(b) ")
#         "return a.name")
# print(list(a))
