# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 01:07:01 2021

@author: Oscar
"""
from check1 import bd

count = 0
count2 = 0
print ('-------------------------') 
for i in bd:
    for j in i:
        if count % 3 == 0:
            print ('|', end = " ")
        print(j, end = " ")
        count += 1
    if count % 3 == 0:
        print ('| ')

    count2 +=1
    if count2 % 3 == 0:
        print ('-------------------------')    
    