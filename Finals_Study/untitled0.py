# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:17:53 2021

@author: Oscar
"""

def merge(L1, L2):
    i1 = 0 
    i2 = 0
    L = []
    done1 = False
    done2 = False
    while not (done1 and done2):
        if not done1 and (done2 or L1[i1]<L2[i2]):
            L.append(L1[i1])
            i1 += 1
            done1 = i1>=len(L1)
        else:
            L.append(L2[i2])
            i2 += 1
            done2 = i2>=len(L2)
        
        return L
    
def merge(L1, L2):
    i1 = 0
    i2 = 0
    L = []
    while i1<= len(L1) and i2<= len(L2):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1+=1 
        elif L1[i1]> L2[i2]:
            L.append(L2[i2])
            i2 +=1
        else:
            L.append(L2[i2])
            i1+=1
            i2+=1
    L.extend(L1[i1:])
    L.extend(L2[i2:])
    return L