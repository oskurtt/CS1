# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:46:06 2021

@author: Oscar
"""
import lab05_util

def print_info(restaurant):
    count = 0
    address = restaurant[3].split("+")
    for i in restaurant[-1]:
        count += i
    count /= 7
    print ("{0} ({1})".format(restaurant[0], restaurant[5]))
    print ("\t\t {0}".format(address[0]))
    print ("\t\t {0}".format(address[1]))
    print("Average score: {:.2f}".format(count))
    
    return

restaurants = lab05_util.read_yelp('yelp.txt')
print (len(restaurants))
while 1==1:
    ask = int(input("Enter ID: "))
    print (ask)
    if ask >=1 and  ask <= 155:     
        print_info(restaurants[ask-1])
    else:
        print ("Warning")