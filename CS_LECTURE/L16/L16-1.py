# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:44:06 2021

@author: Oscar
"""

countries = dict()
countries = {'Algeria': 37.1, 'Canada': 34.9, 'Uganda': 32.9, 'Morocco': 32.7, 'Sudan': 30.9}
# print (len(countries))
# print (sorted(countries.keys()))
# print (sorted(countries.values()))
# print ((countries['Canada']))

countries['Boo'] = 5
print ((countries))
for i in countries.keys():
    print (i)