# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:36:41 2021

@author: Oscar
"""

def find_min(ls):
    order = []
    for i in (ls):
        for j in (i):
            order.append(j)
    return (min(order))
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )