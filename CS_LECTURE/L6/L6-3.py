# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 00:55:44 2021

@author: Oscar
"""

num1 =  float(input("Enter the first number: "))
num11 = "{:g}".format(num1)
print (num11)

num2 =  float((input("Enter the second number: ")))
num22 = "{:g}".format(num2)
print (num22)


if (num1 > 10 and num2 > 10):
    print ("Both are above 10.")
elif (num1 < 10 and num2 <10):
    print ("Both are below 10.")
    
    
avg = (num1 + num2)/2
average = "{:.2f}".format(avg)

print ("Average is", average)