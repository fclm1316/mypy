#!/usr/bin/python3
#coding:utf-8
import csv
input_filename = 'D:/2000Wnew/last50000.csv'
output_filename ='D:/2000Wnew/new50000.csv'

area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古",
      "21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏",
      "33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东",
      "41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西",
      "46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南",
      "54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏",
      "65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
list11 =[]
list12 =[]
list13 =[]
list14 =[]
list15 =[]
list21 =[]
list22 =[]
list23 =[]
list31 =[]
list32 =[]
list33 =[]
list34 =[]
list35 =[]
list36 =[]
list37 =[]
list41 =[]
list42 =[]
list43 =[]
list44 =[]
list45 =[]
list46 =[]
list50 =[]
list51 =[]
list52 =[]
list53 =[]
list54 =[]
list61 =[]
list62 =[]
list63 =[]
list64 =[]
list65 =[]
list71 =[]
list81 =[]
list82 =[]
list91 =[]

def pick_data(filename):
      with open(filename,'r',encoding='gb18030',newline='') as csv_readfile:
          readfile = csv.reader(csv_readfile)
          for aa in readfile:
              if int(aa[2]) == 11:
                  list11.append(aa)
              elif int(aa[2]) == 12:
                  list12.append(aa)
              elif int(aa[2]) == 13:
                  list13.append(aa)
              elif int(aa[2]) == 14:
                  list14.append(aa)
              elif int(aa[2]) == 15:
                  list15.append(aa)
              elif int(aa[2]) == 21:
                  list21.append(aa)
              elif int(aa[2]) == 22:
                  list22.append(aa)
              elif int(aa[2]) == 23:
                  list23.append(aa)
              elif int(aa[2]) == 31:
                  list31.append(aa)
              elif int(aa[2]) == 32:
                  list32.append(aa)
              elif int(aa[2]) == 33:
                  list31.append(aa)
              elif int(aa[2]) == 34:
                  list34.append(aa)
              elif int(aa[2]) == 35:
                  list35.append(aa)
              elif int(aa[2]) == 36:
                  list36.append(aa)
              elif int(aa[2]) == 37:
                  list37.append(aa)
              elif int(aa[2]) == 41:
                  list41.append(aa)
              elif int(aa[2]) == 42:
                  list42.append(aa)
              elif int(aa[2]) == 43:
                  list43.append(aa)
              elif int(aa[2]) == 44:
                  list44.append(aa)
              elif int(aa[2]) == 45:
                  list45.append(aa)
              elif int(aa[2]) == 46:
                  list46.append(aa)
              elif int(aa[2]) == 51:
                  list51.append(aa)
              elif int(aa[2]) == 52:
                  list52.append(aa)
              elif int(aa[2]) == 53:
                  list53.append(aa)
              elif int(aa[2]) == 54:
                  list54.append(aa)
              elif int(aa[2]) == 61:
                  list61.append(aa)
              elif int(aa[2]) == 62:
                  list62.append(aa)
              elif int(aa[2]) == 63:
                  list63.append(aa)
              elif int(aa[2]) == 64:
                  list64.append(aa)
              elif int(aa[2]) == 65:
                  list65.append(aa)
              elif int(aa[2]) == 71:
                  list71.append(aa)
              elif int(aa[2]) == 81:
                  list81.append(aa)
              elif int(aa[2]) == 82:
                  list82.append(aa)
              else :
                  list91.append(aa)


def main():
    pick_data(input_filename)
    for aa in list11:
        print(aa)

if __name__ == '__main__':
    main()


