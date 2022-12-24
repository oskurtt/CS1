# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:02:03 2021

@author: Oscar
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:47:49 2021

@author: Oscar
"""

from tkinter import *
from Ball import *
import random

class BallDraw(object):
    def __init__ (self, parent):
        colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
        self.ls = []
        self.start = []
        for i in range (10):
            x = random.randint(0,400)
            y = random.randint(0,400)
            dx = random.randint(-8,8)
            dy = random.randint(-8,8)
            radius = random.randint(5,10)
            color = random.choice(colorList)
            self.ls.append(Ball(x, y, dx, dy, radius, color))
            self.start.append((x,y))
        
        self.wait_time = 100 
        
        self.isstopped = False 

        self.maxx = 400 
        self.maxy = 400

        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        for i in range(len(self.ls)):
            self.ls.x = self.start[i][0]
            self.ls.y = self.start[i][1]
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        self.canvas.delete("all")
        for i in range(len(self.ls)):
            
            # bounding_box = (self.b.x-self.b.radius, \
            #             self.b.y-self.b.radius,\
            #             self.b.x+self.b.radius, \
            #             self.b.y+self.b.radius) 
            bounding_box = self.ls[i].bounding_box()
            self.canvas.create_oval(bounding_box, fill=self.ls[i].color)
            self.canvas.update()      

        self.canvas.after(self.wait_time)

    def animate(self):
        while not self.isstopped:
                  
                
            self.draw_ball()
            for i in range(len(self.ls)):
                
                self.ls[i].x += self.ls[i].dx
                self.ls[i].y += self.ls[i].dy
                
                self.ls[i].check_and_reverse(self.maxx, self.maxy)
            
            


if __name__ == "__main__":

    root = Tk()
    root.title("Tkinter: Lab 11")

    bd = BallDraw(root)

    bd.animate()

    root.mainloop()


    
