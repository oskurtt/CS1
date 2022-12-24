# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:03:39 2021

@author: Oscar
"""

values = [14, 10, 8, 19, 7, 13]

integer1 = input("Enter a value: ")
print (integer1)

integer2 = input("Enter another value: ")
print (integer2)

values.append(int (integer1))
values.insert(2, int (integer2))

maxlist = max(values)
minlist = min(values)

print (values[3], values[-1])
print ("Difference:", maxlist - minlist)

sumlist = sum(values)
lenlist = len(values)
average = (sumlist/lenlist)
values.sort()

print ("Average: {0:.1f}".format(average))
print ("Median:", ((values[3]+values[4])/2))
