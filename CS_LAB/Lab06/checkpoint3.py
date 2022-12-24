# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:30:15 2021

@author: Oscar
"""

from check1 import bd
from lab06_util import read_sudoku

def pboard(bd):
    count = 0
    count2 = 0
    print ('-------------------------') 
    for i in bd:
        for j in i:
            if count % 3 == 0:
                print ('|', end = " ")
            print(j, end = " ")
            count += 1
        if count % 3 == 0:
            print ('| ')
    
        count2 +=1
        if count2 % 3 == 0:
            print ('-------------------------')    

def ok_to_add(r, c, n, bd1):
    r -= 1
    c -= 1
    for i in bd1[r]:
        for j in i:
            if n == j:
                print("Not Valid1")
                return False
    for i in bd1:
        if n == i[c]:
            print("Not Valid")
            return False
    x = (r//3) * 3
    y = (c//3) * 3
    for i in range(x, x+3):
        for j in range (y, y+3):
            if n == bd1[i][j]:
                print ("Not Valid2")
                return False  
    print ("Valid")
    return True
def verify(bd2):
    for i in bd2:
        for j in i:
            if j == '.':
                return False
name = input("Choose game: ")
board = read_sudoku(name)
pboard(board)
while verify(board) == False: 
    row = int(input("Enter a row: "))
    col = int(input("Enter a column: "))
    num = (input("Enter a num: "))
    if ok_to_add(row, col, num, board) == True:
        board[row-1][col-1] = num
    pboard(board)