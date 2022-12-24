# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:34 2021

@author: Oscar
"""
import json 
from Bear import *
from Tourist import *

class berry (object): 
    def __init__(self, grid, bloc, tloc): 
        self.grid = grid
        self.bloc = bloc
        self.tloc = tloc
        
    def b_check(self, r, c):
        for i in self.bloc:
            if i.r == r and i.c == c:
                return True

    def t_check (self, r, c):
        for i in self.tloc:
            if i.r == r and i.c == c:
                return True

            
    def __str__(self):
        s = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if (self.t_check(i,j)) == True and (self.b_check(i,j) == True):
                    s += ('{:>4}'.format('X'))
                elif (self.b_check(i,j)) == True:
                    s += ('{:>4}'.format('B'))
                elif (self.t_check(i,j)) == True:
                    s += ('{:>4}'.format('T'))
                else:
                    s += ('{:>4}'.format(self.grid[i][j]))
            s += '\n'
        return s
    
    def total_berries(self):
        total = 0
        for i in self.grid:
            total += sum(i)
        return (total) 
    
    def grow (self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if ((type(self.grid[i][j]) == int) and (self.grid[i][j] >= 1) and (self.grid[i][j] < len(self.grid))):
                    self.grid[i][j] = min(self.grid[i][j]+1, 10)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (self.grid[i][j] == 0):
                    if ((i+1) < (len(self.grid))) and (self.grid[i+1][j]==10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)
                    elif ((i-1) != -1) and (self.grid[i-1][j]==len(self.grid)):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)   
                    elif ((j+1)<(len(self.grid))) and (self.grid[i][j+1]==10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)    
                    elif ((j-1) != -1) and (self.grid[i][j-1]==10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)
                    elif ((i+1<(len(self.grid))) and ((j+1)<(len(self.grid)))) and (self.grid[i+1][j+1] == 10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)
                    elif ((i-1!=-1) and (j-1!=-1)) and (self.grid[i-1][j-1] == 10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)   
                    elif ((i+1<(len(self.grid))) and (j-1!=-1)) and (self.grid[i+1][j-1] == 10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10)   
                    elif ((i-1!=-1) and ((j+1)<(len(self.grid)))) and (self.grid[i-1][j+1] == 10):
                        self.grid[i][j] = min(self.grid[i][j]+1, 10) 
    
    