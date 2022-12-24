# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:26:58 2021

@author: Oscar
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
p = float(input("Enter the fraction: "))
print (p)
x = range (len(co2_levels))
for i in x:
    co2_levels[i]= co2_levels[i]*(1+p)

print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))