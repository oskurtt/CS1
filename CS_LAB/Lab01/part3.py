# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:41:53 2021

@author: Oscar
"""
import math

base10size = int(input("Disk size in GB"))
print (base10size)

base2size = math.floor(base10size * (10**9)/(2**30))
print (base2size)

lost_size = (base10size - base2size)
print (lost_size)