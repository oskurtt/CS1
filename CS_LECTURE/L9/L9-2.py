# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:31:11 2021

@author: Oscar
"""

census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
    
i = 1
count1 = 0
count2 = 1

percount1 = 0
percount2 = 1
perlist = []
avgcount = 0

j = 0
avg = 0
avgcount = 0

while i < len(census):
    per = (census[count2]-census[count1])/census[count1]*100
    perlist.append(per)
    i += 1
    count1 += 1
    count2 += 1 

    

while j < 22:

    avg += perlist[avgcount]
    avgcount += 1
    j +=1

avg = avg/22
finavg = ("{:.1f}".format(avg))
print ("Average = ", finavg, "%", sep = "")


