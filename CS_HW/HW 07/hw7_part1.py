# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:29:39 2021

@author: Oscar
"""
def wdfreq_to_dict (file):
    dictionary = dict()
    for i in open(file, encoding = "ISO-8859-1"):
        i = i.strip().split('\n')
        i = i[0].strip().split(',')
        wd = i[0]
        freq = i[1]
        dictionary[wd] = list()
        dictionary[wd].append(freq)
    return dictionary

def key_to_dict (file):
    dictionary = dict()
    for i in open(file, encoding = "ISO-8859-1"):
        i = i.strip().split(' ')
        letter = i[0]
        dictionary[letter] = list()
        for j in range(1,len(i)):
            dictionary[letter].append(i[j])     
    return dictionary

def drop (word, wdfreq):
    word = word.replace(' ','')
    sets = set()
    ls = list(word)
    for j in range(len(ls)):
        x = ls.copy()
        x.pop(j)
        if ''.join(x) in wdfreq:
            sets.add(''.join(x))
    return sets

def insert(word, wdfreq, key):
    word = word.replace(' ','')
    sets = set()
    for i in range(len(word)+1):
        for j in key.keys():
            x = word[:i]+j+word[i:]
            if x in wdfreq:
                sets.add(x)
    return sets

def swap (word, wdfreq):
    word = word.replace(' ','')
    sets = set()
    ls = list(word)
    i = 0
    while i < (len(word)-1):
        x = ls.copy()
        y = ls.copy()
        x[i] = y[i+1]
        x[i+1] = y[i]
        x = ''.join(x)
        if x in wdfreq:
            sets.add(x)
        i+=1
    return sets

def replace (word, wdfreq, key):
    sets = set()
    ls = list(word.replace(' ',''))
    i = 0
    while i < len(ls):
        for j in ls[i]:
            for k in key[j]:
                x = ls.copy()
                x[i] = k
                x = ''.join(x)
                if x in wdfreq:
                    sets.add(x)
        
        i += 1
    return (sets)

    
    
def main():
    dictfile = input('Dictionary file => ')
    # dictfile = ('words_10percent.txt')
    print (dictfile)
    inputfile = input('Input file => ')
    # inputfile = ('input_words.txt')
    print (inputfile)
    keyfile = input('Keyboard file => ')
    # keyfile = ('keyboard.txt')
    print (keyfile)
    
    inwd = (open(inputfile).read().strip().split('\n'))
    wdfreq = wdfreq_to_dict(dictfile)
    wdfreqk = wdfreq.keys()
    key = key_to_dict(keyfile)

        
    for word in inwd:
        lswords = []
        if word in wdfreqk:
            print ('{:>15} -> FOUND'.format(word))
        else:
            if len(drop(word, wdfreqk)) > 0:
                for i in drop(word, wdfreqk):
                    lswords.append((wdfreq[i],i))
            if len(insert(word, wdfreqk, key)) > 0:
                for j in insert(word, wdfreqk, key):
                    lswords.append((wdfreq[j],j))
            if len(swap(word, wdfreqk)) > 0:
                for k in swap(word, wdfreqk):
                    lswords.append((wdfreq[k],k))
            if len(replace(word, wdfreqk, key)) > 0:
                for l in replace(word, wdfreqk, key):
                    lswords.append((wdfreq[l],l)) 
            if len(lswords) == 0:
                print ("{:>15} -> NOT FOUND".format(word))
            else:
                x=[]
                for i in sorted(lswords, reverse = True):
                    x.append(i[1])
                if len(x) > 3:
                    print ('{0:>15} -> FOUND{1:>3}:  {2} {3} {4}'.format(word.replace(' ',''), len(x), x[0], x[1], x[2]))
                else:
                    y = ' '.join(x)
                    print ('{0:>15} -> FOUND{1:>3}:  {2}'.format(word, len(x), y))
    
            


if __name__=="__main__":
    main()