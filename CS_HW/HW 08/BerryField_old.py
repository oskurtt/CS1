# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:34 2021

@author: Oscar
"""
import json

class berry (object): 
    def __init__(self, f): 
        self.data = json.loads(f.read()) 
        self.loc = self.data["berry_field"] #berries only 
        self.ls = self.loc.copy() #berries, bears, and tourists
        self.bears = self.data['active_bears']

    def total_berries(self):
        total = 0
        for i in self.loc:
            total += sum(i)
        return total       
    
    def grid (self):
        for i in self.data['active_bears']:
            self.ls[i[0]][i[1]] = 'B'
        for i in self.data['active_tourists']:
            if self.ls[i[0]][i[1]] != 'B':
                self.ls[i[0]][i[1]] = 'T'
            else:
                self.ls[i[0]][i[1]] = 'X'
        return self.ls
    
    def __str__(self):
        for i in berry.grid(self):
            for j in i:
                print ('{:>4}'.format(j), end="")
            print ('')
        return ('')
            
    def only_berries(self):
        return self.loc
    
    def grow(self):
        for i in range(len(self.loc)):
            for j in range(len(self.loc[i])):
                if ((type(self.loc[i][j]) == int) and (self.loc[i][j] >= 1) and (self.loc[i][j] < 10)):
                    self.loc[i][j] += 1
        for i in range(len(self.loc)):
            for j in range(len(self.loc[i])):
                if (self.loc[i][j] == 0):
                    if ((i+1) < (len(self.loc))) and (self.loc[i+1][j]==10):
                        self.loc[i][j] +=1
                    elif ((i-1) != -1) and (self.loc[i-1][j]==10):
                        self.loc[i][j] += 1   
                    elif ((j+1)<(len(self.loc))) and (self.loc[i][j+1]==10):
                        self.loc[i][j] +=1    
                    elif ((j-1) != -1) and (self.loc[i][j-1]==10):
                        self.loc[i][j] +=1
                    elif (self.loc[i+1][j+1] == 10) and (i+1<(len(self.loc))) and ((j+1)<(len(self.loc))):
                        self.loc[i][j] +=1
                    elif (self.loc[i-1][j-1] == 10) and (i-1!=-1) and (j-1!=-1):
                        self.loc[i][j] +=1    
                    elif (self.loc[i+1][j-1] == 10) and (i+1<(len(self.loc))) and (j-1!=-1):
                        self.loc[i][j] +=1    
                    elif (self.loc[i-1][j+1] == 10) and (i-1!=-1) and ((j+1)<(len(self.loc))):
                        self.loc[i][j] +=1    
        return self.loc