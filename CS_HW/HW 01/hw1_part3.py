# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 15:17:14 2021

@author: Oscar
"""

fchar = input ("Enter frame character ==> ")
print (fchar)

height = input ("Height of box ==> ")
print (height)

width = input ("Width of box ==> ")
print (width)
print ()
space = ((((int(width)-3)-len(width)-len((height))))//2)


print ("Box:")
print (fchar * int (width))
print ((fchar + " "*(int (width)-2) + fchar + "\n")*((int (height)-3)//2), end="")
print (fchar + " "*space + (width) + "x" + (height) + " "*(space+((space+1)%2)) + fchar)
print ((fchar + " "*(int (width)-2) + fchar + "\n")*((int (height)-2)//2), end="")
print (fchar * int (width))

