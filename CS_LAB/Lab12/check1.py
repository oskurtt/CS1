# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:57:29 2021

@author: Oscar
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1

def mult(m,n):
    if n == 0:
        return 0
    if n == 1:
        return m
    else: 
        return mult(m, n-1)+m
    
def power(m,n):
    if n == 0:
        return 1
    if n == 1:
        return m
    else: 
        return power(m, n-1)*m

print (add(6,4))
print (mult(2,3))
print (power(2,4))