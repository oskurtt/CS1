# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:32 2021

@author: Oscar
"""
import json 
from BerryField import *
from Bear import *


class tourist (object):
    def __init__(self, loc):
        self.r = loc[0]
        self.c = loc[1]
        self.turn_no_bear = 0
        self.num_bears = 0
        
    def __str__(self):     
        return("Tourist at ({0},{1}), {2} turns without seeing a bear.".format(self.r, self.c, self.turn_no_bear))
   
    def see_bear (self, AB):
        self.num_bears = 0
        for i in AB:
            if (((i.r-self.r)**2) + ((i.c-self.c)**2)) <= 16:
                self.num_bears += 1
                self.turn_no_bear = 0
    
        if self.num_bears == 0:
            self.turn_no_bear += 1
            
        if (self.turn_no_bear >= 3) or (self.num_bears >=3):
            return ("Went Home")
        