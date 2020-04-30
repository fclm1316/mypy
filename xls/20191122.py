#encoding:utf-8
import xlrd
file1 = 'C:/Users/DC_JL/Desktop/11/华医网卡号.xlsx'
file2 = 'C:/Users/DC_JL/Desktop/11/11.xlsx'
file3 = 'C:/Users/DC_JL/Desktop/11/123.txt'

workbook1 = xlrd.open_workbook(file1)
sheet1 = workbook1.sheet_by_index(0)
cols1 = sheet1.col_values(0)

workbook2 = xlrd.open_workbook(file2)
sheet2 = workbook2.sheet_by_index(0)
cols2 = sheet1.col_values(0)

with open(file3,'w',encoding='gb18030',newline='') as f:
    for i in range(2,1890):
        s2_key = sheet2.cell_value(i,3)
        # print(s2_key)
        for a in range(1,3053):
            s1_key = sheet1.cell_value(a,2)
            s1_value = sheet1.cell_value(a,0)
            if s2_key == s1_key:
                print(s1_value,s1_key)
                f.write('{0:s},{1:s}\n'.format(s1_key,s1_value))

