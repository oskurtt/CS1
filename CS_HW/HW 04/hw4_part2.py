# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:28:18 2021
Create a program that outputs statistics on the spread of COVID 19 in each state
@author: Oscar
"""
from hw4_util import part2_get_week #import necessary functions
from hw4_util import print_abbreviations

    
def covid(w):
    ls = part2_get_week(w) #put output of function into a list
    statels = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",  #create a list of all states 
          "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME",
          "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", 
          "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

    req = (input("Request (daily, pct, quar, high): ").strip()) #ask for input for stats
    print (req)
    req = req.lower()
    
    def dailynum(index): #function to calculate average daily positive cases of the virus
        ls = part2_get_week(w)
        i = 2
        count = 0
        while i >= 2 and i<= 8:
            count += ls[sindex][i]
            i += 1
        count /= 7
        daily = (count/(ls[sindex][1]))*100000
        return daily

    def pctnum(index): #function to calculate the daily percentage of positive cases
        i = 2
        j = 9
        pos = 0
        neg = 0
        while i >= 2 and i<= 8:
            pos += ls[sindex][i]
            i += 1
        while j >= 9 and j <= 15:
            neg += ls[sindex][j]
            j += 1
        pct = (pos/(pos+neg))*100
        return pct
        
    if req == 'daily': #runs if req is == daily
        state = (input("Enter the state: ").strip())     #ask for desired states
        print (state)
        states = state.upper()
        exist = statels.count(states)
        if exist == 1: 
            sindex = statels.index(states) #if state exists, it finds the index in which that state is found in the list
        else:          
            print ("State {} not found".format(state))
            return("...")
        
        print ("Average daily positives per 100K population: {0:.1f}".format(dailynum(sindex))) #print statistic
        return("...")
    
    elif req == 'pct': #same as req == daily but runs pctnum instead of daily num
        state = (input("Enter the state: ").strip())    
        print (state)
        states = state.upper()
        exist = statels.count(states)
        if exist == 1:
            sindex = statels.index(states)
        else:          
            print ("State {} not found".format(state))
            return("...")
        
        print ("Average daily positive percent: {:.1f}".format(pctnum(sindex)))
        return("...")
    
    elif req == 'quar':
        quarls = []
        for i in statels:
            sindex = statels.index(i)
            if  dailynum(sindex) > 10: #append state if its dailynum or pctnum is greater than 10
                quarls.append(i)
            if  pctnum(sindex) > 10:  
                quarls.append(i)
        quarls = list(dict.fromkeys(quarls)) #remove duplicates in list
        print ("Quarantine states:")
        print_abbreviations(quarls) #print states in order with 10 in each row
        return ("...")
    
    elif req == 'high': #find the state with the most number of dailynum cases
        highls = []
        highsls = []
        for i in statels:
            sindex = statels.index(i)
            highls.append(dailynum(sindex))
            highsls.append(i)
            
        print ("State with highest infection rate is {}".format(highsls[highls.index(max(highls))]))
        print ("Rate is {:.1f} per 100,000 people".format(max(highls)))
        return ("...")

    elif req != 'daily' or req != 'pct' or req != 'quar' or req != 'high': #return unrecognized request if input does not match either if statements
        print("Unrecognized request")
        return ("...")

    
def main():
    i = 0    
    print ("...")
    while i == 0: 
    
        index = int(input("Please enter the index for a week: ")) #constantly asks for input and runs function until input is out of desired range
        print (index)
        if index > 29:
            print ("No data for that week")
            print("...")
        elif index <= 0:
            i+=1 #stops asking if index is less than or equal to 0
        else:  
            print (covid(index))

if __name__=="__main__":
    main()