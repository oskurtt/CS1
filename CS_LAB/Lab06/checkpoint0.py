# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 01:09:56 2021

@author: Oscar
"""

line = ""
count1 = 0
count2 = 0
for i in range(0,9):
    line += ("{}".format(i))

for i in line:
    for j in line: 
        if count2 %3 != 0:
            print ("{0},{1}".format(i, j), end = ' ')
            count2 += 1
        else:
            print (" {0},{1:}".format(i, j), end = ' ')
            count2 += 1
        
    print ("")
    count1 += 1
    if count1%3 == 0:
        print ("")
