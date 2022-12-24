# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:42:31 2021

@author: Oscar
"""
import json
from BerryField import berry

class bear (object):
    def __init__(self, f, ls = []):
        self.data = json.loads(f.read())
        self.bearloc = self.data["active_bears"]
        self.berrygrid = ls
        
    def __str__(self):
        for i in self.bearloc:
            print ("Bear at ({0},{1}) moving {2}".format(i[0],i[1],i[2]))
        return ('')
    
    def eat(self, x):
        self.berrygrid = x
        for i in range(len(self.bearloc)):
            eaten = 0
            eaten += self.berrygrid[self.bearloc[i][0]][self.bearloc[i][1]]
            while eaten < 30:
                if bear.move_check(self, i, self.bearloc[i][2]) == True:
                    bear.move(self, i)
                    eaten += self.berrygrid[self.bearloc[i][0]][self.bearloc[i][1]]
                    self.berrygrid[self.bearloc[i][0]][self.bearloc[i][1]] -= min(self.berrygrid[self.bearloc[i][0]][self.bearloc[i][1]],eaten) 
                else:
                    self.bearloc[i][2] = 'exit'
                    eaten = 30
        return self.berrygrid
        
    
    def move (self, i):
        if self.bearloc[i][2] == 'N':
            self.bearloc[i][0] -= 1
        if self.bearloc[i][2] == 'S':
            self.bearloc[i][0] += 1
        if self.bearloc[i][2] == 'E':
            self.bearloc[i][1] += 1
        if self.bearloc[i][2] == 'W':
            self.bearloc[i][1] -= 1
        if self.bearloc[i][2] == 'NE':
            self.bearloc[i][0] -= 1
            self.bearloc[i][1] += 1
        if self.bearloc[i][2] == 'NW':
            self.bearloc[i][0] -= 1
            self.bearloc[i][1] -= 1
        if self.bearloc[i][2] == 'SE':
            self.bearloc[i][0] += 1
            self.bearloc[i][1] += 1
        if self.bearloc[i][2] == 'SW':
            self.bearloc[i][0] += 1
            self.bearloc[i][1] -= 1     
        return self.bearloc[i]
    
    def move_check(self, i, direction):
        if direction == 'N':
            if (self.bearloc[i][0]-1) != -1:
                return True
        if direction == 'S':
            if (self.bearloc[i][0]+1) < len(self.berrygrid):
                return True
        if direction == 'E':
            if (self.bearloc[i][1]+1) < len(self.berrygrid):
                return True
        if direction == 'W':
            if (self.bearloc[i][1]-1) != -1:
                return True
        if direction == 'NE':
            if ((self.bearloc[i][0]-1) != -1) and ((self.bearloc[i][1]+1) < len(self.berrygrid)):
                return True
        if direction == 'NW':
            if ((self.bearloc[i][0]-1) != -1) and ((self.bearloc[i][1]-1) != -1):
                return True
        if direction == 'SE':
            if ((self.bearloc[i][0]+1) < len(self.berrygrid)) and ((self.bearloc[i][1]+1) < len(self.berrygrid)):
                return True
        if direction == 'SW':
            if ((self.bearloc[i][0]+1) < len(self.berrygrid)) and ((self.bearloc[i][1]-1) != -1):
                return True
        pass
    