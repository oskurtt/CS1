# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:09:38 2021

@author: Oscar
"""
i1 = input("Enter the scores file: ")
print (i1)
i2 = input("Enter the output file: ")
print (i2)

ls = []
j = 0

f = open ("{}".format(i1))
f1 = (f.read().split('\n'))

for i in f1:
    if i != "":  
        ls.append(int(i))
    
ls.sort()

f.close()
f = open ("{}".format(i2),"w")
for i in ls:
    f.write("{0:>2}: {1:>3}\n".format(j, i))
    j += 1
