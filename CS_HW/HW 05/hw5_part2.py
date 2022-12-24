# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:12:36 2021
Find the steepest and most gradul path of each grid
Then print a grid of the frequencies of the coordinates that have been pathed before
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
def organize2(grid):
    for i in grid:
        for j in i:
            print("{:>3}".format(j), end = "")
        print ("")
    return j
def get_nbers(startloc, row, col): #get neighboring coordinates
   ls = []
   if startloc[0]-1 >= 0:
       ls.append((startloc[0]-1, startloc[1]))

   if startloc[1]-1 >= 0:
       ls.append((startloc[0], startloc[1]-1))

   if startloc[1]+1 <= col-1:
       ls.append((startloc[0], startloc[1]+1))

   if startloc[0]+1 <= row-1:
       ls.append((startloc[0]+1, startloc[1]))
   return ls    
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
            
def globalmax(x): #find global max
    ls = []
    for i in x:
        for j in i:
            ls.append(j) #append all values of grid into a list
            
    for i in x:
        for j in i:    
            if x[x.index(i)][i.index(j)] == max(ls): #find max of the list
                print ("global max: ({0}, {1}) {2}".format(x.index(i), i.index(j), max(ls)))
                
                
def steep (grid, startloc, maxstep, pathls, pathgrid):
    neighbors = get_nbers(startloc, len(getgrid), column(getgrid)) #find neighbors of said coordinates
    nextloc = startloc #next location to find neighbors

    for i in range(len(neighbors)):
        cval = grid[nextloc[0]][nextloc[1]] #current value
        nval = grid[neighbors[i][0]][neighbors[i][1]] #next value
        if ((nval - grid[startloc[0]][startloc[1]]) <= maxstep) and (nval > cval): #compare the two values with set conditions
            nextloc = neighbors[i] #set nextloc to the next coordinate
            
    if (nextloc == startloc): #if location doesn't move, just end function
        return 
    else:
        pathls.append(nextloc) #append locations into a path
        steep(grid, nextloc, maxstep, pathls, pathgrid) #run function steep again
        pathgrid[nextloc[0]][nextloc[1]] += 1 #add 1 to the pathgrid to add 'frequency'
     
def grad (grid, startloc, maxstep, pathls, pathgrid): 
    neighbors = get_nbers(startloc, len(getgrid), column(getgrid)) 
    nextloc = startloc
    sval = grid[startloc[0]][startloc[1]] #start value
    change = False
    for i in range(len(neighbors)):
        cval = grid[nextloc[0]][nextloc[1]]
        nval = grid[neighbors[i][0]][neighbors[i][1]]
        if change == False:   #if change is false
            if ((nval - grid[startloc[0]][startloc[1]]) <= maxstep) and (nval > cval):
                nextloc = neighbors[i]
                change = True #change to true
        elif change == True:
            if cval > nval and nval > sval: #if the next value fit logic
                diff = nval - sval #find difference
                if maxstep >= diff: 
                    nextloc = neighbors[i] #set nextloc to next coordination
            
    if (nextloc == startloc):
        return 
    else:
        pathls.append(nextloc) #does same at function steep()
        grad(grid, nextloc, maxstep, pathls, pathgrid)
        pathgrid[nextloc[0]][nextloc[1]] += 1

        
def localmax(grid, steepls): #find localmax and if false, print no max
    neighbors = get_nbers(steepls, len(getgrid), column(getgrid))
    for i in neighbors:
        if (grid[steepls[0]][steepls[1]]) < (grid[i[0]][i[1]]):
            return False
    return True

def main(): 
    while True:
        global grid
        global getgrid
        grid = int(input("Enter a grid index less than or equal to 3 (0 to end): ")) # input gird number
        print (grid)
        
        startloc = hw5_util.get_start_locations(grid)
        getgrid = hw5_util.get_grid(grid)
        
        if grid == 0:
            break
        while grid > 3: #keeps asking until condition is met
            grid = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
            print (grid)
        
        maxstep = int(input("Enter the maximum step height: "))
        print (maxstep)
            
        pgrid = input("Should the path grid be printed (Y or N): ") #asks to print grid or not
        print (pgrid)
        
        print ("Grid has {0} rows and {1} columns".format(len(getgrid), column(getgrid)))     
            
        globalmax(getgrid)
        
        globalls = [] #global max variable
        for i in getgrid:
            for j in i:
                globalls.append(j)
        maxval = max(globalls)
        
        pathgrid = [] #create the pathgrid with 0s
        for i in range(len(getgrid)):
            ls = []
            for j in range(len(getgrid[i])):
                ls.append(0)
            pathgrid.append(ls)
        
        for i in startloc: #print steep and grad coordinations
            pathgrid[i[0]][i[1]] += 1
            pathgrid[i[0]][i[1]] += 1
            steepls = []
            steepls.append(i)
            steep(getgrid, i, maxstep, steepls, pathgrid)
            print ("===")
            print ("steepest path")
            for j in range(len(steepls)):
                print(steepls[j],end = ' ')
                if (j-4)% 5== 0 and j >3: #prints line after printing every five coordinates
                    print()

            if getgrid[steepls[-1][0]][steepls[-1][1]] == maxval: #print global, no, or local maximum
                print ("\nglobal maximum")
            elif localmax(getgrid, steepls[-1]) == False:
                print ("\nno maximum")
            else:
                print ('\nlocal maximum')
                
            print ("...")
            
            gradls = [] #same as steep 
            gradls.append(i)
            grad(getgrid, i, maxstep, gradls, pathgrid)
            print ("most gradual path")
            
            for k in range(len(gradls)):
                print(gradls[k],end = ' ')
                if (k-4)% 5== 0 and k >3:
                    print()
                    
            if getgrid[gradls[-1][0]][gradls[-1][1]] == maxval:
                print ("\nglobal maximum")
            elif localmax(getgrid, gradls[-1]) == False:
                print ('\nno maximum')
            else:
                print ("\nlocal maximum")
                
        print ('===')
        for i in range(len(pathgrid)): #if path grid still have 0s, change to .
            for j in range(len(pathgrid[i])):
                if pathgrid[i][j] == 0: 
                    pathgrid[i][j] = '.'
        if pgrid == 'Y' or pgrid == 'y': #if answered yes, print grid
            print ("Path grid")
            organize2(pathgrid)
        break
    
if __name__=="__main__":
    main()