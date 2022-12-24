# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:41:10 2021

@author: Oscar
"""
import json 
from BerryField import berry
from Bear import bear
from Tourist import tourist

def main():
    file = input("Enter the json file name for the simulation => ")
    # file = "bears_and_berries_1.json"
    print (file)
    
    # data = json.loads(f.read())
    # print(data["berry_field"])
    # print(data["active_bears"])
    # print(data["reserve_bears"])
    # print(data["active_tourists"])
    # print(data["reserve_tourists"])
    
    berries = berry(open(file))
    bears = bear(open(file))
    tourists = tourist(open(file))
    print ("")
    
    print ("Field has {} berries.".format(berry.total_berries(berries)))
    berry.__str__(berries)
    print ('')
    
    print ("Active Bears:")
    bear.__str__(bears)
    print ('')
    
    print ("Active Tourists:")
    tourist.__str__(tourists)
    
    
if __name__=="__main__":
    main()