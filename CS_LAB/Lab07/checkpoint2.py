# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:11:54 2021

@author: Oscar
"""
u = [0, 1, 2, 3, 4, 5, 6]
v = ["a","b","c","d","e","f","g","h","i","j",
"k","l","m","n","o","p","q","r","s","t",
"u","v","w","x","y","z"]

x = u[::2] + v[1:len(v)//2:2]
print (x)