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
    file = input("Enter the json file name for the simulation => ")
    # file = ("bears_and_berries_2.json")
    print (file)
    f = open(file)
    data = json.loads(f.read())
    
    AB = []
    AT = []
    RB = []
    RT = []
    for i in data["reserve_bears"]:
        RB.append(bear(i))
    for i in data["reserve_tourists"]:
        RT.append(tourist(i))
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
    
    turns = 1
    run = True
    while run == True:
        print ("Turn: {0}".format(turns))
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
        
        if (len(RB)>0) and (berry.total_berries(BF) >= 500):
            AB.append(RB[0])
            print ('Bear at ({0},{1}) moving {2} - Entered the Field'\
                   .format(RB[0].r,RB[0].c, RB[0].d ))
            RB.pop(0)
            
        if (len(RT)>0) and (len(AB)>0):
            AT.append(RT[0])
            print ('Tourist at ({0},{1}), {2} turns without seeing a bear. - Entered the Field'\
                   .format(RT[0].r,RT[0].c, RT[0].turn_no_bear))
            RT.pop(0)    
        print ('\n')
        
        if turns %5 == 0:
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
        turns += 1
        if (len(AB) == 0 and len(RB) == 0) or (len(AB)==0 and berry.total_berries(BF) ==0):
            run = False
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