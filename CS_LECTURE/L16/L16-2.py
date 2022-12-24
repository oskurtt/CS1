# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:53:08 2021

@author: Oscar
"""

imdb_file = ("imdb_data.txt").strip()
print (imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
limit = len(names)
counter = 0
maxval = 0
for index in range(limit):
    name = names[index]
    if counts[name] > maxval:
       maxval = counts [name]
       maxname = name
    if counts[name] == 1:
       counter += 1
print("{0} appears most often: {1} times".format(maxname, maxval))    
print ("{} people appear once".format(counter))
