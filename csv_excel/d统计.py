#!/usr/bin/python3
# coding:utf-8
from collections import Counter
import os
import csv
import pandas as pd
import json
from collections import Counter

header_list = ['WORKDATE', 'REFID', 'SEQNO', 'TRNCODE', 'CLASSID',
               'PRESDATE', 'PRESTIME', 'ORIGINATOR', 'ACCEPTOR', 'DCFLAG',
               'NOTETYPE', 'NOTENO', 'CURCODE', 'CURTYPE', 'ISSUEDATE',
               'SETTLAMT', 'ISSUEAMT', 'REMNAMT', 'PAYINGACCT', 'PAYER',
               'PAYINGBANK', 'PCBANK', 'BENEACCT', 'BENENAME', 'BENEBANK',
               'BCBANK', 'AGREEMENT', 'PURPOSE', 'MEMO', 'TERMTYPE',
               'TERMID', 'ACCTOPER', 'AUDITOR', 'AUTHDEVID', 'PAYKEY',
               'TESTKEY', 'WORKROUND', 'CLEARDATE', 'CLEARROUND', 'EXCHGDATE',
               'EXCHGROUND', 'CLEARTIME', 'CLEARSTATE', 'ERRCODE', 'FEEPAYER',
               'FEECODE', 'FEE', 'TRUNCFLAG', 'CLEARAREA', 'EXCHAREA',
               'ROUTEID', 'PRESAREA', 'ACPTAREA', 'EXTRADATAFLAG', 'ATTACHFILE',
               'RESERVED']

file_path = 'd:/data/'

for root, dir, files in os.walk(file_path):
    for file in files:
        file_name = os.path.join(root, file)

        files = os.path.basename(file_name).split('.')
        if files[1] == 'vsc':
            # print(file_name)
            with open(file_name, 'r', encoding='gb18030', newline='') as file:
                print(file_name)
                filereader = pd.read_csv(file, encoding='utf-8', low_memory=False, names=header_list)
                filedict = os.path.join(file_name.split('.')[0] + '.' + 'txt')
                # print(filedict)
                with open(filedict, 'w') as dict_file:
                    # dataframe 计数
                    # dict_file.write(str(dict(filereader['PCBANK'].value_counts())))
                    S = filereader['PCBANK'].value_counts()
                    # datafram 转 json
                    to_json = S.to_json()
                    dict_file.write(str(to_json))
                    # print(filedict)
                # list_aa = []
                # for aa in filereader['PAYINGBANK']:
                #     list_aa.append(str(aa)[0:6])
                #
                # print(Counter(list_aa))

                # filesssss = pd.DataFrame(filereader[['PCBANK','WORKDATE','REFID']])
                # print(filesssss.isnull().any())
                # list_a = []
                # for aaa in filereader['PCBANK']:
                #     list_a.append(aaa)
                # print(list_a)

# if __name__ == "__main__":
#     pass
