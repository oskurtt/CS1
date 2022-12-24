# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:36:58 2021

@author: Oscar
"""
dale = int(input("Enter Dale's height: "))
print (dale)
erin = int(input("Enter Erin's height: "))
print (erin)
sam = int(input("Enter Sam's height: "))
print (sam)

if dale > erin and dale > sam:
    print ("Dale")
if erin > dale and erin > sam:
    print ('Erin')
if sam > dale and sam > erin:
    print ("Sam")

if (dale > erin and dale < sam) or (dale < erin and dale > sam):
     print ("Dale")
if (erin > dale and erin < sam) or (erin > sam and erin < dale):
    print ("Erin")
if (sam > dale and sam < erin) or (sam > erin and sam < dale):
    print ("Sam")
    
if (dale < sam and dale < erin):
    print ("Dale")
    
if (erin < sam and erin < dale):
    print ("Erin")
    
if (sam < dale and sam < erin):
    print ("Sam")