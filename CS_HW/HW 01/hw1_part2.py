# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:03:28 2021

@author: Oscar
"""
import math

minutes = (input ("Minutes ==> "))
minutes1 = int (minutes)
print (minutes)
seconds = ((input ("Seconds ==> ")))
seconds1 = int(seconds)
print (seconds)
miles = (input (("Miles ==> ")))
miles1 = float(miles)
print (miles)
targmiles = input ("Target Miles ==> ")
targmiles1 = float (targmiles)
targmiles2 = "{:.2f}".format(targmiles1)
print (targmiles)
print ("")

pacetime = (((minutes1 * 60) + seconds1)/ miles1)
pacemin = (pacetime//60)
paceminround = "{:g}".format(pacemin)
pacesec = ((pacetime%60))
pacesecround = math.floor (pacesec)
print ("Pace is", paceminround, "minutes and", pacesecround, "seconds per mile.")

speed = 60/(pacemin + (((pacesec*100)/60)/100))
speedfin = '{0:.2f}'.format(speed)
speedfin1 = float(speedfin)
print ("Speed is", speedfin, "miles per hour.")

timemin = (targmiles1/speedfin1)*60
timeminint = timemin//1
timeminint1 = "{:g}".format(timeminint)
timesec = (((timemin*60)-(timeminint*60)))

print ("Time to run the target distance of", targmiles2, "miles is", 
       timeminint1, "minutes and", timesec, "seconds.")
