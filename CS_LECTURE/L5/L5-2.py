# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:17:43 2021

@author: Oscar
"""
def frame_string (word):
    length = len(word)
    print ("*"*3+ "*"*length+ "*"*3)
    print ("**", word, "**")
    print ("*"*3+ "*"*length+ "*"*3)
    return ("")
    
print (frame_string("Spanish Inquisition"))    
print (frame_string("Ni"))
