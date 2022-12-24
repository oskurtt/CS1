# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:37:02 2021

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
list = get_words(file.read())
print('File {0} {1} words'.format(f,len(list)))
print(list)
