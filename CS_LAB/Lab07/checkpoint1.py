# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:21:14 2021

@author: Oscar
"""
ls = []
finls = []
count = 1
def parse_line(txt):
    ls = (txt.split('/'))
    if ls[-1].isnumeric() and ls[-2].isnumeric() and ls[-3].isnumeric():
        finls.append(ls[-3])
        finls.append(ls[-2])
        finls.append(ls[-1])
        finls.append(ls[0]+'/'+(ls[1]))
        print (finls)
    else:
        print ('None')
    
parse_line("Here is some random text, like 5/4=3./12/3/4")