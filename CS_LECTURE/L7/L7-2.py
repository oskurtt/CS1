# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:45:00 2021

@author: Oscar
"""

def add_tuples (x, y, z):
    zeroval = (x[0]+y[0]+z[0])
    oneval = (x[1]+y[1]+z[1])
    return (zeroval, oneval)
    
print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))
