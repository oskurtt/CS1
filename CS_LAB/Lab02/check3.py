# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:14:06 2021

@author: Oscar
"""

fname = input ("Please enter your first name: ")
lname = input ("Please enter your last name: ")
lname1 = (lname+"!")
hello = "Hello,"

lfname = len(fname)
llname = len(lname1)
lhello = len("Hello,")

x = max (lfname, llname, lhello)
print (x)

print (("*"*x)+6*"*")
print ("**", hello + (" "*(x-lhello)), "**")
print ("**", fname + (" "*(x-lfname)), "**")
print ("**", lname1 + (" "*(x-llname)), "**")
print (("*"*x)+6*"*")