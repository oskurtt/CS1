# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:27:17 2021

@author: 97075
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
file = open(f)
set1 = get_words(file.read())
print('File {0} {1} words'.format(f,len(set1)))
print(set1)

f2 = input("Enter another file name ")
file2 = open(f2)
set2 = get_words(file2.read())
print('File 2 {0} {1} words'.format(f2,len(set2)))
print(set2)


print('Comparing clubs wrpi and csa:')
print('Same words: {}'.format(set1&set2))
print('unique to {0}: {1}'.format(f,set1-set2))
print('unique to {0}: {1}'.format(f2,set2-set1))