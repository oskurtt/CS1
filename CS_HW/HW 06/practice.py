# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 03:02:26 2021

@author: Oscar
"""

def parse_txt (f):
    file = open(f)
    list = []
    ls = []
    x = file.read().split('\n')
    y = []
    z = []
    for i in x:
        y.append(i.split(' '))
    for i in range(len(y)):
        for j in range(len(y[i])):
            z.append(y[i][j])
    for i in z:
        list.append(i)
    for i in range(len(list)):
        whitelist = set("abcdefghijklmnopqrstuvwxyz")
        list[i] = list[i].lower()
        list[i] = ''.join(filter(whitelist.__contains__, list[i]))
    for i in list:
        if i != '':
            ls.append(i)
    return ls

# def parse_stop (f):
#     file = open(f)
#     list = []
#     for i in file.read().split('\n'):
#         list.append(i)
        
#     return list

def remove_stop_words(stop, ls):
    for i in stop:
        for j in ls:
            if i == j:
                ls.remove(j)
    return ls

doc1 = 'cat_in_the_hat.txt'

doc2 = 'ex2.txt'

wdlensum1 = 0
ls1 = (parse_txt(doc1))
ls2 = (parse_txt(doc2))
stop = (parse_txt('stop.txt'))
ls1 = list(dict.fromkeys((remove_stop_words(stop, ls1))))
ls2 = list(dict.fromkeys((remove_stop_words(stop, ls2))))
print (len(ls1))