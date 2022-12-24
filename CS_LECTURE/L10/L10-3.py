# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:58:54 2021

@author: Oscar
"""
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
count = 0
avg = sum(co2_levels)/len(co2_levels)

for i in co2_levels:
    if i > avg:
        count += 1
      
print ("Average: {:.2f}".format(avg))
print ("Num above average: {:d}".format(count))
