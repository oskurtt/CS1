# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:41:10 2021

@author: Oscar
"""
import json 
from BerryField import *
from Bear import *
from Tourist import *

def main():
    # file = input("Enter the json file name for the simulation => ")
    file = ("bears_and_berries_1.json")
    print (file)
    f = open(file)
    data = json.loads(f.read())
    
    AB = []
    AT = []
    for i in data["active_bears"]:
        AB.append(bear(i))
    for i in data["active_tourists"]:
        AT.append(tourist(i))  
    BF = berry(data['berry_field'], AB, AT)
    
    print ('')
    print ("Starting Configuration")
    print("Field has {} berries.".format(berry.total_berries(BF)))
    print(str(BF))
    
    print ("Active Bears:")
    for i in AB:
        print (str(i))
    print ('')
    
    print ("Active Tourists:")
    for i in AT:
        print (str(i))
    print ('')
    
    for i in range(0,5):
        print ("Turn: {0}".format(i+1))
        (BF.grow())
        removing = set()
        for j in AB:
            if (j.eat(BF, AT)) == "Exit":
                print ("Bear at ({0},{1}) moving {2} - Left the Field". format(j.r, j.c, j.d))
                removing.add(j)
        for r in removing:
            AB.remove(r)
        
        removing2 = set()
        for k in AT:
            if k.see_bear(AB) == "Went Home":
                print ("Tourist at ({0},{1}), {2} turns without seeing a bear. - Left the Field"\
                       .format(k.r, k.c, k.turn_no_bear))
                removing2.add(k)
        for r2 in removing2:
            AT.remove(r2)
            
        print("Field has {} berries.".format(berry.total_berries(BF)))
        print(str(BF))

        print ("Active Bears:")
        for i in AB:
            print (str(i))
        print ('')
    
        print ("Active Tourists:")
        for i in AT:
            print (str(i))
        print ('')
if __name__=="__main__":
    main()