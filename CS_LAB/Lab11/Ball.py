# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:23:53 2021

@author: Oscar
"""

class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    
    def bounding_box(self):
        return (self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx,maxy):
        if 0 < self.x + self.radius and \
              self.x - self.radius < maxx and \
              0 < self.y + self.radius and \
              self.y - self.radius < maxy:
            return True
        else:
            return False
    
    def check_and_reverse (self, maxx, maxy):
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= maxx):
            self.dx = -self.dx
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= maxy):
            self.dy = -self.dy