# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:12:49 2021
Finding strength and statistics of passwords
@author: Oscar
"""

import hw4_util
import re

def length(word):
    count = 0
    if len(word) == 6 or len(word) == 7: #if length of word is a certain length, add a certain value to count
        count += 1
    elif len(word) == 8 or len(word) == 9 or len(word) == 10:
        count += 2
    elif len(word) > 10:
        count += 3
    if count == 0 :
        return "None"
    if count > 0:
        return (count)
    
def cases(word):
    countcap = 0
    countlow = 0
    count = 0
    for i in word: 
        if i.isupper(): #counts number of capital letters
            countcap += 1 
        if i.islower(): #counts number of lower case letters
            countlow += 1
    if countcap >= 2 and countlow >= 2: #add to count accordingly
        count += 2
    elif countcap >= 1 and countlow >= 1:
        count += 1
    if count == 0:
        return "None"
    return (count)

def digits(word):
    count = 0
    digit = 0
    for i in word:
        if i.isdigit() == True: #check if each letter/number is a digit
            digit += 1
    if digit >= 2:
        count += 2
        return (count)
    elif digit >= 1: #add count if there is atleast one number
        count += 1
        return (count)
    if count == 0:
        return "None"
    
        
def punctuation1(word):
    count = 0
    for i in word:
        if i == '!' or i == '@' or i == '#' or i == '$': #looks for punctuations
            count += 1
    if count == 0:
            return "None"
    return min(count, 1)
    
def punctuation2(word):
    count = 0
    for i in word:
        if i == '%' or i == '^' or i == '&' or i == '*': #looks for more punctuations
            count += 1
    if count == 0:
            return "None"
    return min(count, 1)

def ny(word):
    count = 0
    word = word.lower()
    words = re.match("[a-z][a-z][a-z][0-9][0-9][0-9][0-9]", word) #finds this format
    if bool(words) == True:
        count -= 2
        return (count)

    if count == 0:
        return "None"
def commons(word):
    count = 0
    word = word.lower()
    words = hw4_util.part1_get_top() 
    for i in words:   #look for words in the "get top" list
        if word == i:
            count -= 3
    if count == 0:
            return "None"
    return (count)

def main():
        
    combined = 0
    p = input("Enter a password => ") 
    print (p)
    word = p.strip()
    
    
    if length(word) != "None": #if returns none, don't print, if not, print the value
        print ("Length: +{}".format(length(word)))
    if cases(word) != "None":
        print ("Cases: +{}".format(cases(word)))
    if digits(word) != "None":
        print ("Digits: +{}".format(digits(word)))
               
    if punctuation1(word) != "None":
        print ("!@#$: +{}".format(punctuation1(word)))
        
    if punctuation2(word) != "None":
        print ("%^&*: +{}".format(punctuation2(word)))
        
    if ny(word) != "None":
        print ("License: {}".format(ny(word)))
    
    if commons(word) != "None":
        print ("Common: {}".format(commons(word)))
        
    if length(word) != "None": #add each functions count all together
        combined +=length(word)
    if cases(word) != "None":
        combined +=cases(word)
    if digits(word) != "None":
        combined +=digits(word)     
    if punctuation1(word) != "None":
        combined +=punctuation1(word)
    if punctuation2(word) != "None":
       combined +=punctuation2(word)
    if ny(word) != "None":
       combined +=ny(word)
    if commons(word) != "None":
        combined +=commons(word)
        
    print ("Combined score: {}".format(combined))
    
    if combined <= 0: #tells user strength of password
        print ("Password is rejected")
    if combined == 1 or combined == 2 :
        print ("Password is poor")
    if combined == 3 or combined == 4:
        print ("Password is fair")
    if combined == 5 or combined == 6:
        print ("Password is good")
    if combined >= 7:
        print ("Password is excellent")

if __name__=="__main__":
    main()