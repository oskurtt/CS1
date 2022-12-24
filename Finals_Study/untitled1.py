# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 01:28:01 2021

@author: Oscar
"""

# def framed(name):
#     n = max( len("Hello!"), len(name) )
#     print("*" * (n+4))
#     print("* " + "Hello!".center(n) + " *")
#     print("* " + name.center(n) + " *")
#     print("*" * (n+4))
# framed("kj")
# L1 = [ 1, 3, 5, 6, 7, 8, 10 ]
# L2 = [ 5, 6, 10, 13, 14 ]

def cmp_string(s):
    return len(s),s
L = [ "apple", "ball", "car", "card", "basket", "car", "honey" ]
L.sort(key = cmp_string)

print(L)