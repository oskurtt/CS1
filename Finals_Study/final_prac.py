# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:07:02 2021

@author: Oscar
"""

# def make_runs(v):
#     L = []
#     ls = [v[0]]
#     if len(v) == 0:
#         return L
#     for i in range(1,len(v)):
#         if v[i] >= ls[-1]:
#             ls.append(v[i])
#         else:
#             L.append(ls)
#             ls = [v[i]]
#     L.append(ls)
#     return L

# # def make_runs(L):
# #     if len(L) == 0:
# #         return(L)
# #     newL = []
# #     localL = [L[0]]
# #     for index in range(1, len(L)):
# #         if L[index] >= localL[-1]:
# #             localL.append(L[index])
# #         else:
# #             newL.append(localL)
# #             localL = [L[index]]
# #     newL.append(localL)
# #     return newL
# print( make_runs( [7, 5, 9, 11, 2, 6, 10, 18, 19, 17] ))

file = ('final.txt')
file2 = ('Output.txt')
file = open(file, 'r')
file2 = open(file2, 'w')
one = file.readline()
two = file.read()
file2.write(one)
file2.write(two)