#!/usr/bin/python3
#coding:utf-8
import sys ,os,requests,re
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool

try:
    input_url_all = sys.argv[1]
except Exception:
    print('url')
    sys.exit()
input_url = os.path.splitext(input_url_all)[0]
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/70.0.3538.77 Safari/537.36'}
def get_page(url):
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            response.encoding = 'UTF-8'
            return response.text
        return response.status_code
    except RequestException:
        return None

def mysoup(html_soup):
    soup = BeautifulSoup(html_soup,'lxml')
    # print(soup('div',attrs={'class':'news_warp_center'}))
    soup_hot = soup.find_all('div',attrs={'class':'news_warp_center'})
    #print(soup_hot)
    pattern = re.compile(r'.*?src="(.*?)".*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern,str(soup_hot))
    for type,name in items:
        type_new = os.path.splitext(type)
        name = str(name).replace('?','')
        print(name)
        writ_to_file(name,type_new[1],type)

def writ_to_file(name,type,files):
    file_name = ''.join(name+type)
    file_content = requests.get(files)
    with open(file_name,'wb') as f:
        f.write(file_content.content)
        f.close()

def page48(html_pattern):
    pattern = re.compile('<p align="center">.*?img src="(.*?)" alt=.*?</p>',re.S)
    items = re.findall(pattern,str(html_pattern))
    return items

def main(pageno):
    print(pageno)
    url = input_url + '_' + str(pageno) + '.html'
    html = get_page(url)
    mysoup(html)

def main1(page):
    url = input_url + '_' + '48' + '.html'
    html = get_page(url)
    print(page)
    for item in page48(html):
        name = os.path.splitext(item)[0].split('_')[1]
        type = os.path.splitext(item)[1]
        print(name)
        writ_to_file(name,type,item)

if __name__ == '__main__':
    # for i in range(2,48):
    #     main(i)
    pool = Pool()
    pool.map(main,[i for i in range(2,48)])
    main1(48)

