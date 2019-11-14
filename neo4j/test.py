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
from py2neo import Graph,Node,Relationship

g = Graph("bolt://localhost:7687",user='neo4j',password='root123')
test_node_1 = Node("Person",name = "test_node_1")
test_node_2 = Node("Person",name = "test_node_2")
test_node_3 = Node("Bank",name = "test_node_3")
test_node_4 = Node("Bank",name = "test_node_4")
noed_know1 = Relationship(test_node_1,"单项",test_node_2)
noed_know2 = Relationship(test_node_3,"单项",test_node_4)
noed_know3 = Relationship(test_node_3,"单项",test_node_1)
noed_know4 = Relationship(test_node_4,"单项",test_node_1)
g.create(test_node_1)
g.create(test_node_2)
g.create(test_node_3)
g.create(test_node_4)
g.create(noed_know1)
g.create(noed_know2)
g.create(noed_know3)
g.create(noed_know4)
