# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:27:27 2021

@author: Oscar
"""
def get_words(string):
    s=set()
    string=string.replace(',',' ')
    string=string.replace('.',' ')
    string=string.replace('(',' ')
    string=string.replace(')',' ')
    string=string.replace('"',' ')
    string=string.replace('|',' ')
    l=string.split(' ')
    for i in l:
        if len(i)>=4 and i.isalpha():
            s.add(i.lower())
    return s

f = input("Enter the file name ")
print (f)
file = open(f).read()
set1 = get_words(file)


file2 = open('allclubs.txt').read()
file2 = file2.strip().split('\n')
x = []
for line in file2:
    count = 0
    clubwords = get_words(line)
    count += len(set1&clubwords)
    x.append((count, (line.split('|')[0])))
    
x = sorted(x, reverse = True)
print (x[0])
print (x[1])
print (x[2])
print (x[3])
print (x[4])

    

