#encoding:utf-8
from __future__ import division
import sys
import time

def progressbar(do,all_do,prefix='',size=60,file=sys.stdout):
    def show(j):
        x = do/all_do
        a = int(x*size)
        # b = int((1-x)*size)
        b = size - a
        file.write("%s[%s%s] %i/%i\r" % (prefix, ">"*a, "."*b, do , all_do))
        file.flush()

    show(do)
    file.write("\n")
    file.flush()
