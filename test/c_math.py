# encoding:utf-8
# File: c_math.py
# Author:fbi
# Time: 20/12/24
import random,openpyxl

# a = [random.randint(0,21) for _ in range(3)]
list_all = []

while len(list_all) <= 840:
    a = [_ for _ in range(21)]
    list_a = sorted(random.sample(a, 3))
    max_num = list_a[2]
    mid_num = list_a[1]
    min_num = list_a[0]
    if max_num + mid_num + min_num >= 20:
        if mid_num + min_num > max_num:
            if mid_num + min_num > 20:
                list_all.append('{}-{}+{}='.format(max_num, mid_num, min_num))
                # list_all.append('{}-{}+{}={}'.format(max_num, mid_num, min_num,max_num-mid_num+min_num))
            else:
                list_all.append('{}+{}-{}='.format(min_num, mid_num, max_num))
                # list_all.append('{}+{}-{}={}'.format(min_num, mid_num, max_num,min_num+mid_num-max_num))
        else:
            if mid_num + min_num > 10:
                list_all.append('{}-{}+{}='.format(max_num, mid_num, min_num))
                # list_all.append('{}-{}+{}={}'.format(max_num, mid_num, min_num,max_num-mid_num+min_num))
            else:
                list_all.append('{}-{}-{}='.format(max_num, min_num, mid_num))
                # list_all.append('{}-{}+{}={}'.format(max_num, mid_num, min_num,max_num-mid_num+min_num))
    else:
        list_all.append('{}+{}+{}='.format(max_num, mid_num, min_num))
        # list_all.append('{}+{}+{}={}'.format(max_num, mid_num, min_num,max_num+mid_num+min_num))

file_xlsx = 'C:/Users/DC_JL/Desktop/c_math.xlsx'
wookbook = openpyxl.Workbook()
sheet = wookbook.worksheets[0]
k = 0
for i in range(1,16,2):
    for j in range(1,210,2):
        k = k + 1
        sheet.cell(row=j,column=i).value = list_all[k]
wookbook.save(file_xlsx)
