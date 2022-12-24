# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:38:10 2021

@author: Oscar
"""
from syllables import find_num_syllables #import function from module

def hard_words (ls): #function to find hard words
    hardls = []
    for i in ls: 
        if ((i.find("-") == -1) and i[len(i)-2] + i[-1] != "es" and i[len(i)-2] + i[-1] != "ed" and (find_num_syllables(i) >= 3)): 
            #checks to see that no hyphen exists, the last two letters of the word is no es or ed and the word also have 3 syllables
            hardls.append(i)
    return hardls #adds the word to the list and returns it

def avg_syllables(ls):
    count = 0 #count total number of syllables
    for i in ls:
        count += find_num_syllables(i) #adds number of syllables of each word to store in count and returns it
    return count

     
paragraph = input("Enter a paragraph => ")
lswords = paragraph.split() #splits paragraph into each separate word
lsperiod = paragraph.split(". ") #only splits paragraph into each different sentences

hardwords = hard_words(lswords) #prints hard words
asl = len(lswords)/len(lsperiod) #prints asl
phw = (len(hardwords)/len(lswords))*100 #prints PHW
asyl = avg_syllables(lswords)/len(lswords) #prints asyl
gfri = 0.4*(asl + phw) #prints gfri
fkri = 206.835-1.015*asl-86.4*asyl #prints fkri

print(paragraph)
print ("Here are the hard words in this paragraph:\n{}".format(hardwords))
print ("Statistics: ASL:{0:.2f} PHW:{1:.2f}% ASYL:{2:.2f}".format(asl, phw, asyl))
print ("Readability index (GFRI): {0:.2f}\nReadability index (FKRI): {1:.2f}".format(gfri, fkri))
