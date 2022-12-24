# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:32:01 2021

@author: Oscar
"""

imdb_file = ('imdb_data.txt').strip()
print(imdb_file)

movies = dict()
oui = ''
# for line in open(imdb_file, encoding = "ISO-8859-1"):
#     words = line.strip().split('|')
#     name = words[0].strip()
#     movie = words[1].strip()
#     if movie in movies:
#         movies[movie].add(name)
#     else:
#         movies[movie] = set()
#         movies[movie].add(name)

# count = 0
# x = 0
# countname = ''
# for i in movies.keys():
#     if count < len(movies.get(i)):
#         count = len(movies.get(i))
#         countname = i
#     if len(movies.get(i)) == 1:
#         x += 1
# print (count)
# print (countname)
# print (x)

for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    print (words)
    # print (name)