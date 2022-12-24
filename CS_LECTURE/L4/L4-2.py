# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 02:13:54 2021

@author: Oscar
"""

import math

r1 = round(5)
r2 = 32

aarea1 = ((math.pi)*r1**2)
Area1 = '{0:.2f}'.format(aarea1)
print ("Area 1 =", Area1)

aarea2 = ((math.pi)*pow(r2,2))
Area2 = '{0:.2f}'.format(aarea2)
print ("Area 2 =", Area2)