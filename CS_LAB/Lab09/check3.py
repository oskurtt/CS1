# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:07:41 2021

@author: Oscar
"""

from Date import Date

bdfile = open('birthdays.txt').read().strip().split('\n')
bdls = []
for line in bdfile:
    line = line.split()
    d = Date(line[0],line[1],line[2])
    bdls.append(d)

x = sorted(bdls)
ls = [0]*13
for i in x:
    # print (str(i))
    ls[int(i.m)] += 1
    
    
print (bdls[0])
print (bdls[-1])
print (ls.index(max(ls)))
# print (bdls)
# for i in bdfile:
#     print (i[0])
#     # d = Date(i[0)
#     # print (d)