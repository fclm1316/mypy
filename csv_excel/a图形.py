#!/usr/bin/python3
# coding:utf-8
from pyecharts import Bar

out_path = 'd:/data/'
dict_sum = {'2010': 473669, '2011': 602910, '2012': 569211,
            '2013': 527294, '2014': 462602, '2015': 423780,
            '2016': 400474, '2017': 371426, '2018': 373545}


def bar_tu(dict, html_name, path):
    bar = Bar('统计', '数量')
    bar.add('数量', list(dict.keys()), list(dict.values()), xaxis_name='时间',
            is_label_show=True)
    bar.render(''.join(path + html_name + '.html'))


if __name__ == "__main__":
    bar_tu(dict_sum, '年', out_path)
