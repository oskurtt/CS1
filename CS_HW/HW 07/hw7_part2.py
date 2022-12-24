# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:25:21 2021

@author: Oscar
"""

import json

def main():
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    minyear = input("Min year => ")
    # minyear = '2000'
    print (minyear)
    maxyear = input("Max year => ")
    # maxyear = '2016'
    print (maxyear)
    w1 = input("Weight for IMDB => ")
    # w1 = '0.7'
    print (w1)
    w2 = input("Weight for Twitter => ")
    # w2 = '0.3'
    print (w2)
    print ('')
    
    genre = input("What genre do you want to see? ")
    print (genre)
    print ('')
    
    sets = set()
    for ID in movies.keys():
        for i in movies[ID]['genre']:
            sets.add(i)     
            
    while genre.lower() != 'stop':
        if genre.title() not in sets:
            print ('No {0} movie found in {1} through {2}'.format(genre.title(), minyear, maxyear))
            print ('')
            genre = input("What genre do you want to see? ")
            print (genre)
            print ('')
            continue
        
        else:
            ls = []
            for ID in movies.keys():
                twitter = 0 
                if ID in ratings.keys():
                    if (genre.title() in movies[ID]['genre']) and (int(minyear) <= movies[ID]['movie_year'] <= int(maxyear)) and (len(ratings[ID]) >= 3) and (ID in ratings.keys()): 
                        for i in ratings[ID]:
                            twitter += i
                        twitter = twitter/len(ratings[ID])
                        rating = ((float(w1) * movies[ID]['rating']) + (float(w2) * twitter)) / (float(w1) + float(w2))
                        ls.append((rating, movies[ID]['name'], movies[ID]['movie_year']))
            if ls == []:
                print ('No {0} movie found in {1} through {2}'.format(genre.title(), minyear, maxyear))
                print ('')
                genre = input("What genre do you want to see? ")
                print (genre)
                continue
            ls = sorted(ls)
            ls = sorted(ls, reverse = True)
            print ("Best:")
            print ("        Released in {0}, {1} has a rating of {2:.2f}".format(ls[0][2], ls[0][1], ls[0][0]))
            print ('')
            print ("Worst:")
            print ("        Released in {0}, {1} has a rating of {2:.2f}".format(ls[-1][2], ls[-1][1], ls[-1][0]))
            print ('')
            
            genre = input("What genre do you want to see? ")
            print (genre)
            if genre.lower() != 'stop':
                print ('')

        
if __name__=="__main__":
    main()