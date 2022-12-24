# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:32 2021

@author: Oscar
"""
import json

class tourist (object):
    def __init__(self, f):
        self.data = json.loads(f.read())
        self.loc1 = self.data["active_tourists"]
        
    def __str__(self):
        for i in self.loc1:
            print ("Tourist at ({0},{1}), 0 turns without seeing a bear.".format(i[0],i[1]))
        return ('')
    
