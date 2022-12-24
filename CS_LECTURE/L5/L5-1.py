# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:27:12 2021

@author: Oscar
"""

def convert2fahren (temp):
    fahrenheit = ((temp*(9/5))+32)
    return (fahrenheit)

print ("0 ->", convert2fahren(0))
print ("32 ->",convert2fahren(32))
print ("100 ->",convert2fahren(100))

