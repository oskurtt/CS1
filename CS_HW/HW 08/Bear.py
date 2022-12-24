# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:31 2021

@author: Oscar
"""
import json 
from BerryField import *
from Tourist import *

class bear (object):
    def __init__(self, loc):
        self.r = loc[0]
        self.c = loc[1]
        self.d = loc[2]
        self.asleep = False
        self.aslturns = 3
        
    def __str__(self):
        if self.asleep == True:
            return ('Bear at ({0},{1}) moving {2} - Asleep for {3} more turns'.format(self.r,self.c,self.d,self.aslturns))
        else:
            return("Bear at ({0},{1}) moving {2}".format(self.r, self.c, self.d))
    
    def eat (self, BF, AT):
        eaten = 0
        for i in AT:
            if (self.r == i.r) and (self.c == i.c):
                self.asleep = True
                print ("Tourist at ({0},{1}), {2} turns without seeing a bear. - Left the Field"\
                       .format(i.r, i.c, i.turn_no_bear))
                AT.remove(i)
                
        while (eaten <= 30) and (self.asleep == False):
            preveat = eaten
            eaten += BF.grid[self.r][self.c]
            BF.grid[self.r][self.c] = max(0, BF.grid[self.r][self.c]-(30-preveat))
            if eaten >= 30:
                break
            self.move()
            for i in AT:
                if (self.r == i.r) and (self.c == i.c):
                    self.asleep = True
                    print ("Tourist at ({0},{1}), {2} turns without seeing a bear. - Left the Field"\
                           .format(i.r, i.c, i.turn_no_bear))
                    AT.remove(i)
            if not self.check_move(BF.grid):
                return ("Exit")
        
        if self.asleep == True:
            self.aslturns -= 1
            if self.aslturns == 0:
                self.asleep = False
                self.aslturns = 3
    
    def tourist_check(self, AT):
        for i in AT:
            if (self.r == i.r) and (self.c == i.c):
                self.asleep = True
                print ("Tourist at ({0},{1}), {2} turns without seeing a bear. - Left the Field"\
                       .format(i.r, i.c, i.turn_no_bear))
                AT.remove(i)
                return "DED"
    def move (self):
        if self.d == 'N':
            self.r -= 1
        if self.d == 'S':
            self.r += 1
        if self.d == 'E':
            self.c += 1
        if self.d == 'W':
            self.c -= 1
        if self.d == 'NE':
            self.r -= 1
            self.c += 1
        if self.d == 'NW':
            self.r -= 1
            self.c -= 1
        if self.d == 'SE':
            self.r += 1
            self.c += 1
        if self.d == 'SW':
            self.r += 1
            self.c -= 1     
            
    def check_move(self, grid):
        return self.r >= 0 and self.r < len(grid) and self.c >= 0 and self.c < len(grid[0])
        # if self.d == 'N':
        #     if (self.r-1) != -1:
        #         return True
        # if self.d == 'S':
        #     if (self.r+1) < len(grid):
        #         return True
        # if self.d == 'E':
        #     if (self.c+1) < len(grid):
        #         return True
        # if self.d == 'W':
        #     if (self.c-1) != -1:
        #         return True
        # if self.d == 'NE':
        #     if ((self.r-1) != -1) or ((self.c+1) < len(grid)):
        #         return True
        # if self.d == 'NW':
        #     if ((self.r-1) != -1) or ((self.c-1) != -1):
        #         return True
        # if self.d == 'SE':
        #     if ((self.r+1) < len(grid)) or ((self.c+1) < len(grid)):
        #         return True
        # if self.d == 'SW':
        #     if ((self.r+1) < len(grid)) or ((self.c-1) != -1):
        #         return True