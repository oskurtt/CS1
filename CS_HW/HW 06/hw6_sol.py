# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:31:41 2021
Comapring words and statistics of two files.
You parse each file, sort it, and remove stop words.
Then you find the average length of each list
Find ratio of distinct and non-distinct words
Create a list of each word with the same length of letters
Create a list of word pairs for a chosen maximum step
Find ratio of distinct word pairs to non-distinct word pairs
Finally, compare the word lengths of each file, the similarity of its words and its words by length, 
word pair similarity
@author: Oscar
"""
def parse_txt (f): #parsing text
    file = open(f) #opens file
    list = []
    ls = []
    x = file.read().split('\n') #splits the list by each line first
    y = []
    z = []
    for i in x:
        y.append(i.split(' ')) #split the spaces
    for i in range(len(y)):
        for j in range(len(y[i])):
            z.append(y[i][j]) #append each individual word
    for i in z:
        list.append(i) #append z to another list
    for i in range(len(list)):
        whitelist = set("abcdefghijklmnopqrstuvwxyz") #make a list of alphabets
        list[i] = list[i].lower() #make all lowercase
        list[i] = ''.join(filter(whitelist.__contains__, list[i])) #only keep alphabets in word
    for i in list:
        if i != '':
            ls.append(i) #append word if it's not 'nothing'
    return ls

def remove_stop_words(stop, ls): 
    for i in ls: 
        if i in stop:
            ls.remove(i) #if the word exists in stop file, remove it
    return ls

def word_set (wdlen, ls): 
    list = []
    for i in ls:
        if len(i) == wdlen: #checks if length of word is equal to chosen word length
            list.append(i) #if it is, append it
    list.sort() #sort the order of words
    return list

def max_letters (ls): 
    count = 0
    for i in ls:
        count = max(count, len(i)) #checks length of each word and return maximum
    return count

def main():
    doc1 =input("Enter the first file to analyze and compare ==> ") #input name of docs
    print (doc1)
    doc2 =input("Enter the second file to analyze and compare ==> ")
    print (doc2)
    maxstep = int(input("Enter the maximum separation between words in a pair ==> ")) #input maxstep
    print (maxstep)
    print ('')
    
   
    ls1 = set(parse_txt(doc1)) #distinct list
    ls2 = set(parse_txt(doc2))
    ls1n = parse_txt(doc1) #non-distinct 
    ls2n = parse_txt(doc2)
    stop = set(parse_txt('stop.txt')) #parse the stop words file
    # ls1 = list(dict.fromkeys(stop))
    # ls2 = list(dict.fromkeys(stop))
    ls1 = [i for i in ls1 if i not in stop] #remove stop words
    ls2 = [i for i in ls2 if i not in stop]
    ls1n = [i for i in ls1n if i not in stop]
    ls2n = [i for i in ls2n if i not in stop]
    
    #1
    print ("Evaluating document {}".format(doc1))
    wdlensum1 = 0
    for i in ls1n:
        wdlensum1 += (len(i)) #find sum of lengths of each word
    print ("1. Average word length: {0:.2f}".format(wdlensum1/len(ls1n))) #total length/number of words
    #2
    ratio1 = len(ls1)/len(ls1n) #divides length of distinct list by non-distinct list
    print ("2. Ratio of distinct words to total words: {0:.3f}".format(ratio1)) 
    #3
    print ("3. Word sets for document {}:".format(doc1))
    for i in range (1,max_letters(ls1)+1): #for i in maximum length of the words in the list
        if len((word_set(i, ls1))) >= 7: #if there are too many words, only return first three and last three words
            print ("{0:>4}:{1:>4}: ".format(i, len(word_set(i, ls1))), end = '')
            for j in range (0,3):#prints first three
                print ((word_set(i, ls1))[j], end = " ")
            print ("...", end = " ")
            for k in range(3,0,-1): #prints last three
                if k == 1:
                    print ((word_set(i, ls1))[-k])
                else:
                    print ((word_set(i, ls1))[-k], end = " ")

        else: #print list normally if under 7 words
            if word_set(i, ls1) == []:
                print ("{0:>4}:{1:>4}:".format(i, len(word_set(i, ls1))))
            else:
                print ("{0:>4}:{1:>4}:".format(i, len(word_set(i, ls1))), end = ' ')
                for j in (word_set(i, ls1)):
                    if j == (word_set(i, ls1))[-1]:
                        print (j)
                    else:
                        print (j, end = ' ')

    #4
    print ("4. Word pairs for document {}".format(doc1))
    wdpairs = []
    index = 0
    while index < len(ls1n): #keeps looping until end of list
        for j in range(maxstep):#j is range of maxsteps
            if (j+index+1) < len(ls1n): #if the word being added is not outside of length of list
                x = sorted((ls1n[index],ls1n[j+index+1])) #sort the pair
                wdpairs.append((x[0],x[1])) #append the pair
        index += 1
    
    dwdpairs = set(wdpairs) #list of distinct word pairs
    dwdpairs = sorted(dwdpairs) 
    dwdpairs = list(dwdpairs)
    nwdpairs = wdpairs #list of non-distinct word pairs
    print ("  {} distinct pairs".format(len(dwdpairs)))
    if len(dwdpairs)>5: #if there are more than 5 pairs, print the first five and last five
        for i in range(0,5):
            print ("  {0} {1}".format(dwdpairs[i][0], dwdpairs[i][1]))
        print ('  ...')
        for i in range(5,0, -1):
            print ("  {0} {1}".format(dwdpairs[-i][0], dwdpairs[-i][1]))
    else:
        for i in range(0,5):
            print ("  {0} {1}".format(dwdpairs[i][0], dwdpairs[i][1]))
    #5
    print ('5. Ratio of distinct word pairs to total: {:.3f}'.format(len(dwdpairs)/len(nwdpairs))) #length of distinct word pairs list/length of non-distinct word pairs list
    print ('')
    
    
    
    #exactly the same as code above but for second list
    #1 
    print ("Evaluating document {}".format(doc2))
    wdlensum2 = 0
    for i in ls2n:
        wdlensum2 += (len(i))
    print ("1. Average word length: {0:.2f}".format(wdlensum2/len(ls2n)))
    #2
    ratio2 = len(ls2)/len(ls2n)
    print ("2. Ratio of distinct words to total words: {0:.3f}".format(ratio2))
    #3
    print ("3. Word sets for document {}:".format(doc2))
    for i in range (1,max_letters(ls2)+1):
        if len((word_set(i, ls2))) >= 7:
            print ("{0:>4}:{1:>4}: ".format(i, len(word_set(i, ls2))), end = '')
            for j in range (0,3):
                print ((word_set(i, ls2))[j], end = " ")
            print ("...", end = " ")
            for k in range(3,0,-1):
                if k == 1:
                    print ((word_set(i, ls2))[-k])
                else:
                    print ((word_set(i, ls2))[-k], end = " ")

        else:
            if word_set(i, ls2) == []:
                print ("{0:>4}:{1:>4}:".format(i, len(word_set(i, ls2))))
            else:
                print ("{0:>4}:{1:>4}:".format(i, len(word_set(i, ls2))), end = ' ')
                for j in (word_set(i, ls2)):
                    if j == (word_set(i, ls2))[-1]:
                        print (j)
                    else:
                        print (j, end = ' ')

    #4
    print ("4. Word pairs for document {}".format(doc2))
    wdpairs2 = []
    index2 = 0
    while index2 < len(ls2n):
        for j in range(maxstep):
            if (j+index2+1) < len(ls2n):
                x = sorted((ls2n[index2],ls2n[j+index2+1]))
                wdpairs2.append((x[0],x[1]))
        index2 += 1
    
    dwdpairs2 = set(wdpairs2) #list of distinct word pairs
    dwdpairs2 = sorted(dwdpairs2)
    dwdpairs2 = list(dwdpairs2)
    nwdpairs2 = wdpairs2 #list of non-distinct word pairs
    print ("  {} distinct pairs".format(len(dwdpairs2)))
    if len(dwdpairs2)>5:
        for i in range(0,5):
            print ("  {0} {1}".format(dwdpairs2[i][0], dwdpairs2[i][1]))
        print ('  ...')
        for i in range(5,0, -1):
            print ("  {0} {1}".format(dwdpairs2[-i][0], dwdpairs2[-i][1]))  
    else:
        for i in range(0,5):
            print ("  {0} {1}".format(dwdpairs2[i][0], dwdpairs2[i][1]))
    #5
    print ('5. Ratio of distinct word pairs to total: {:.3f}'.format(len(dwdpairs2)/len(nwdpairs2)))
    print ('')
    
    
    
    #sum 1
    print ("Summary comparison")
    if (wdlensum2/len(ls2n)) > (wdlensum1/len(ls1n)): #find which list has longer words
        print ("1. {} on average uses longer words than {}".format(doc2, doc1))
    else:
        print ("1. {} on average uses longer words than {}".format(doc1, doc2))
    #sum 2
    l1 = set(ls1)
    l2 = set(ls2) #turns list to a set to use union and intersection function
    print ("2. Overall word use similarity: {:.3f}".format(len(l1.intersection(l2))/len(l1.union(l2)))) #Jaccard's formula
    #sum 3
    print ('3. Word use similarity by length:')
    for i in range (1,max(max_letters(ls1), max_letters(ls2))+1):
        if len(set((word_set(i, ls1))).union(set((word_set(i, ls2))))) == 0: #if function is being divided by zero, just return zero
            print ("{0:>4}: 0.0000".format(i)) 
        else:
            print ("{0:>4}: {1:.4f}".format(i, (len(set((word_set(i, ls1))).intersection(set((word_set(i, ls2)))))/len(set((word_set(i, ls1))).union(set((word_set(i, ls2))))))), end = '\n')
    #print out Jacard's function for word list
    #sum 4
    dwdpairs = set(dwdpairs)
    dwdpairs2 = set(dwdpairs2)
    print ("4. Word pair similarity: {:.4f}".format(len(dwdpairs.intersection(dwdpairs2))/len(dwdpairs.union(dwdpairs2))))
    #Jacard's function but uses word pairs
if __name__=="__main__":
    main()