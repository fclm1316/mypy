#!/usr/bin/python3
#coding:utf-8
import sys
import csv
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
header_list =['WORKDATE','REFID','SEQNO','TRNCODE','CLASSID','PRESDATE','PRESTIME','ORIGINATOR',\
              'ACCEPTOR','DCFLAG','NOTETYPE','NOTENO','CURCODE','CURTYPE','ISSUEDATE',\
              'SETTLAMT','ISSUEAMT','REMNAMT','PAYINGACCT','PAYER','PAYINGBANK','PCBANK',\
              'BENEACCT','BENENAME','BENEBANK','BCBANK','AGREEMENT','PURPOSE','MEMO','TERMTYPE',\
              'TERMID','ACCTOPER','AUDITOR','AUTHDEVID','PAYKEY','TESTKEY','WORKROUND','CLEARDATE',\
              'CLEARROUND','EXCHGDATE','EXCHGROUND','CLEARTIME','CLEARSTATE','ERRCODE','FEEPAYER',\
              'FEECODE','FEE','TRUNCFLAG','CLEARAREA','EXCHAREA','ROUTEID','PRESAREA','ACPTAREA',\
              'EXTRADATAFLAG','ATTACHFILE','RESERVED']
#data_frame = pd.read_csv(input_file,header=1,names=header_list,\
#                         encoding='gb18030',low_memory=False)
#data_frame.to_csv(output_file,index=False,encoding='gb18030')
with open(input_file,'r+',encoding='gb18030') as f:
    content = f.read()
    f.seek(0,0)
    f.write(str(header_list)+content)
