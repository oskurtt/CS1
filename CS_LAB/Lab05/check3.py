# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:56:59 2021

@author: Oscar
"""

import lab05_util
import webbrowser
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
    
    q = int(input("""What would you like to do next?
1. Visit the homepage
2. Show on Google Maps
3. Show directions to this restaurant
Your choice (1-3)? ==> """))
    
    if q == 1:
        webbrowser.open(restaurant[-3])
    if q == 2:
        webbrowser.open('http://www.google.com/maps/place/{0} {1}'.format(address[0], address[1]))
    if q == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/{0} {1}'.format(address[0], address[1]))
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