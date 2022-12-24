# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:37:29 2021

@author: Oscar
"""

sentence = input("Enter a sentence => ")
print (sentence)

def number_happy (sentence):
    happy = ("laugh", "happiness", "love", "excellent", "good", "smile")
    counter = 0
    for i in happy:
            counter += sentence.lower().count(i)
    return (counter * "+")

def number_sad (sentence):
    sad = ("bad", "sad", "terrible", "horrible", "problem", "hate")
    counter = 0
    for i in sad:
            counter += sentence.lower().count(i)
    return (counter * "-")


print ("Sentiment:", number_happy(sentence) + number_sad(sentence))
 
if len (number_happy(sentence)) > len (number_sad(sentence)):
    print ("This is a happy sentence.")
elif len (number_sad(sentence)) > len (number_happy(sentence)):
        print ("This is a sad sentence.")
else:
    print ("This is a neutral sentence.")
