# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:12:36 2021
Asks user for a grid number and user chooses to print or not print grid. Then code will output
rows and columns of grid and its neighboring coordates as well as determining if selected path is valid
and if so, how much the change of downward and upward are
@author: Oscar
"""
import hw5_util

def column(grid): #find number of grid
    for i in grid:
        j = len(i)
    return j

def organize(grid): #organizes grid in rows and columns
    for i in grid:
        for j in i:
            print("{:>4}".format(j), end = "")
        print ("")
    return j

def get_nbers(row, col): #get neighboring coordinates
    j = 0
    ls = (hw5_util.get_start_locations(grid))
    
    for i in ls:
        coord1 = []
        coord2 = []
        coord3 = []
        coord4 = []
        
        coord1x = (ls[j][0]) -1   
        coord1y = (ls[j][1]) 
        coord1.append(coord1x)
        coord1.append(coord1y)
        
        coord2x = (ls[j][0]) 
        coord2y = (ls[j][1]) -1 
        coord2.append(coord2x)
        coord2.append(coord2y)
        
        coord3x = (ls[j][0]) +1
        coord3y = (ls[j][1])  
        coord3.append(coord3x)
        coord3.append(coord3y)
        
        coord4x = (ls[j][0]) 
        coord4y = (ls[j][1]) +1 
        coord4.append(coord4x)
        coord4.append(coord4y)
        
        coord1txt = " {}".format(tuple(coord1))
        coord2txt = " {}".format(tuple(coord2))
        coord3txt = " {}".format(tuple(coord3))
        coord4txt = " {}".format(tuple(coord4))
        if (coord1[0] < 0) or (coord1[0] > (len(hw5_util.get_grid(grid)))-1) or (coord1[1] < 0) or (coord1[1] > column(hw5_util.get_grid(grid))-1):
            coord1txt = ""    
        if (coord2[0] < 0) or (coord2[0] > (len(hw5_util.get_grid(grid)))-1) or (coord2[1] < 0) or (coord2[1] > column(hw5_util.get_grid(grid))-1):
            coord2txt = "" 
        if (coord3[0] < 0) or (coord3[0] > (len(hw5_util.get_grid(grid)))-1) or (coord3[1] < 0) or (coord3[1] > column(hw5_util.get_grid(grid))-1):
            coord3txt = ""    
        if (coord4[0] < 0) or (coord4[0] > (len(hw5_util.get_grid(grid)))-1) or (coord4[1] < 0) or (coord4[1] > column(hw5_util.get_grid(grid))-1):
            coord4txt = ""
        print ("Neighbors of ({0}, {1}):{2}{3}{5}{4}".format(ls[j][0], ls[j][1], coord1txt, coord2txt, coord3txt, coord4txt))
        j += 1
        
def valid(x): #check to see if path is valid and if so how much it has moved up, down, left or right
    
    d = 0
    u = 0
    path = True
    for i in range(len(x)-1):
        
        num1 = hw5_util.get_grid(grid)[x[i][0]][x[i][1]]
        num2 = hw5_util.get_grid(grid)[x[i+1][0]][x[i+1][1]]
        if (x[i][0] == x[i+1][0] or x[i][1] == x[i+1][1]):
            
            if num2 < num1:
                d += (num1 - num2)
                
            elif num2 > num1:
                u += (num2 - num1)
        else:
            print ("Path: invalid step from {} to {}".format(x[i], x[i+1]))
            path = False
            break
    if path == True:
        print ("Valid path")
        print ("Downward {}".format(d))
        print ("Upward {}".format(u))
            
def main(): 
    while True:
        global grid
        grid = int(input("Enter a grid index less than or equal to 3 (0 to end): ")) # input gird number
        print (grid)
        
        if grid == 0:
            break
        while grid > 3: #keeps asking until condition is met
            grid = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
            print (grid)
        pgrid = input("Should the grid be printed (Y or N): ") #asks to print grid or not
        print (pgrid)
        if pgrid == 'Y' or pgrid == 'y':
            print ("Grid {}".format(grid))
            organize(hw5_util.get_grid(grid))
            
        print ("Grid has {0} rows and {1} columns".format(len(hw5_util.get_grid(grid)), column(hw5_util.get_grid(grid)))) 
        
        get_nbers(len(hw5_util.get_grid(grid)), column(hw5_util.get_grid(grid)))#print neighbor coordinates
        
        valid(hw5_util.get_path(grid)) #print if path is valid or not
        break
    
if __name__=="__main__":
    main()