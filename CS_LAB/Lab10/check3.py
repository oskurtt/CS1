# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:16:27 2021

@author: Oscar
"""
import random
import time

def closest1 (list):
    '''
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    '''
    ls = []
    ls2 = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            val = abs(list[i]-list[j])
            ls.append(list[i])
            ls.append(list[j])
            ls.append(val)
            ls2.append(val)
    ind = (ls.index(min(ls2)))
    return (ls[ind-2], ls[ind-1])

def closest2 (list):
    ls = []
    ls2 = []
    listt = sorted(list)
    for i in range(len(listt)-1):
        val = abs(listt[i]-listt[i+1])
        ls.append(listt[i])
        ls.append(listt[i+1])
        ls.append(val)
        ls2.append(val)
    ind = (ls.index(min(ls2)))
    return (ls[ind-2], ls[ind-1])
    
if __name__ == "__main__":
    ls1 = []
    for i in range(0, 10000):
        ls1.append(random.uniform(0,1000))
    
    s1 = time.time()
    result = closest2(ls1)
    t1 = time.time() - s1
    print(t1)

    # s2 = time.time()
    # result2 = closest2(list(random.uniform(0, 1000)))
    # t2 = time.time() - s2
    # print(t2)