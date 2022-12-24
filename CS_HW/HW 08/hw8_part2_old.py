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
    # file = input("Enter the json file name for the simulation => ")
    file = "bears_and_berries_1.json"
    print (file)
    
    # data = json.loads(f.read())
    # print(data["berry_field"])
    # print(data["active_bears"])
    # print(data["reserve_bears"])
    # print(data["active_tourists"])
    # print(data["reserve_tourists"])
    
    berries = berry(open(file))
    berries2 = berry(open(file))
    bears = bear(open(file))
    tourists = tourist(open(file))
    print ("")
    
    
    print ("Field has {} berries.".format(berry.total_berries(berries))) #prints total berries and grid
    str(berries)
    print ('')
    
    print ("Active Bears:")
    str(bears)
    print ('')

    print ("Active Tourists:")
    str(tourists)
    print ('')
    
    for i in range(5):
        print ('Turn: {}'.format(i+1))
        (berry.grow(berries)) #grid with bears & tourists
        (berry.grow(berries2)) #grid with only num of berries
        # print(bear.eat(bears, berry.only_berries(berries2)))
        # str(bears)
        print ("Field has {} berries.".format(berry.total_berries(berries2))) #prints total berries
        str(berries) #prints the grid with bears & tourists
        # print (berry.only_berries(berries2))

        

    
if __name__=="__main__":
    main()