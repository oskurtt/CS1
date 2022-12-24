# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:06:54 2021

@author: Oscar
"""

def linear_search( x, L ):
    if x in L:
        return L.index(x)
    else:
        if x < L[0]:
            return (0)
        if x > L[-1]:
            return (len(L))
        else:
            for i in range(len(L)):
                if L[i+1] > x > L[i]:
                    L.insert(i+1,x)
            return L.index(x)

if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = linear_search(x, values )
            print(loc)