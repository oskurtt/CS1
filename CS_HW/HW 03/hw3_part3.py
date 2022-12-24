# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:08:54 2021

@author: Oscar
"""
import math 

def tourists_num(bears):
    if math.floor(bears) < 4 or math.floor(bears) > 15:
        tourists = 0
        return tourists
    else:
        if math.floor(bears) >= 10:
            tourists = 20000*(math.floor(bears)-10) + 100000
        else:
            tourists = 10000*math.floor(bears)
        return tourists

def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)
    return (math.floor(bears_next), berries_next)

lsbears = []
lsberries = []
lstourists = []

bears = int(input("Number of bears => "))
print (bears)
berries = (input ("Size of berry area => "))
print ((berries))
berries = float(berries)
tourists = tourists_num(bears)

print ("{:<10s}{:<10s}{:<10s}{:<10s}".format("Year", "Bears", "Berry", "Tourists"))
print ("{:<10s}{:<10}{:<10}{:<10}".format("1", bears, berries, tourists)) #"1", bears, berries, tourists
lsbears.append(bears)
lsberries.append(berries)
lstourists.append(tourists)
i = 1
while i < 10:
    tourists = tourists_num(bears)
    x = find_next(bears, berries, tourists_num(bears))
    lsbears.append(x[0])
    bears = (x[0])
    if (x[1] < 0):
        berries = 0
    else:
        berries = x[1]
    lsberries.append(berries)
    lstourists.append(tourists_num(bears))
    i += 1
    
    print ("{:<10}{:<10}{:<10.1f}{:<10}".format(i, bears, round(berries, 1), tourists_num(bears)))
print ("")
print ("{:<10s}{:<10}{:<10.1f}{:<10}".format("Min:",min(lsbears), min(lsberries), min(lstourists)))
print ("{:<10s}{:<10}{:<10.1f}{:<10}".format("Max:",max(lsbears), max(lsberries), max(lstourists)))


