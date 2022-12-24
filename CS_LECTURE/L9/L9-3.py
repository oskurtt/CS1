# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:45:56 2021

@author: Oscar
"""

ls = []
num = int((input("Enter a value (0 to end): ")))
print (num)
ls.append(num)

while num != 0:
    num = int((input("Enter a value (0 to end): ")))
    print (num)
    ls.append(num)

ls.remove(0)

print ("Min:", min(ls))
print ("Max:", max(ls))

i = 0 
count = 0
total = 0
while i < len(ls):
    total += ls[count]
    i += 1
    count += 1


avg = total/len(ls)
print ("Avg: {0:.1f}".format(avg))