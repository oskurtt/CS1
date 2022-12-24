# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:03:41 2021

@author: Oscar
"""

import lab05_util

# def print_info(restaurant):
#     count = 0
#     address = restaurant[3].split("+")
#     for i in restaurant[-1]:
#         count += i
#     count /= 7
#     print ("{0} ({1})".format(restaurant[0], restaurant[5]))
#     print ("\t\t {0}".format(address[0]))
#     print ("\t\t {0}".format(address[1]))
#     print("Average score: {:.2f}".format(count))
    
#     return

# restaurants = lab05_util.read_yelp('yelp.txt')
# print_info(restaurants[0])

for line in open('yelp.txt'):
    print (line)