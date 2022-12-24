# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:01:27 2021

@author: Oscar
"""
#calculate the number of target gumballs, side length of machine, extra gumballs left and the wasted space of the machine


import math

def find_volume_sphere (radius):
    return (4/3)*math.pi*(radius**3)
    #volume of sphere formula
def find_volume_cube(side):
    return (side**3)
    #volume of cube formula
pradius = input("Enter the gum ball radius (in.) => ")
print (pradius)
radius = float (pradius)

pweekly_sales = input("Enter the weekly sales => ")
print (pweekly_sales + "\n")
weekly_sales = float (pweekly_sales)

    #asks user to input values
if radius == 0:
    targetgum = 0
    sidelength = 0
    totalgum = 0
    extragum = 0
    wastedspace = 0
    wastedspace1 = 0
    edgegum = 0

else:
    targetgum = math.ceil(weekly_sales * 1.25) #roundup the amount of weekly sales by 1.25
    sidelength = (math.ceil(targetgum**(1/3))*(2*radius)) #find cube root of target gumballs and multiplying it by the diameter of each ball
    edgegum = math.ceil(sidelength/(2*radius)) #how many gumballs fit each side
    extragum = ((edgegum**3)-targetgum) #how many gumballs are in the machine minus the target gumballs to find extra balls
    wastedspace = ((find_volume_cube(sidelength))-(find_volume_sphere(radius)*targetgum)) #volume of cube - volume of sphere to find leftover space 
    wastedspace1 = ((find_volume_cube(sidelength))-(find_volume_sphere(radius)*(edgegum**3)))

    
print ("The machine needs to hold {0} gum balls along each edge.\nTotal edge length is {1:.2f} inches.\nTarget sales were {2}, but the machine will hold {3} extra gum balls.\nWasted space is {4:.2f} cubic inches with the target number of gum balls,\nor {5:.2f} cubic inches if you fill up the machine.".format(edgegum, sidelength, targetgum, extragum, wastedspace, wastedspace1))
           
           
           