"""
This program experiments with the use of functions
and also learning error checking.


"""

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
import math

def line_length(x1,y1,x2,y2):
    length = (int (x1) - int(x2))**2 + (int(y1)- int(y2))**2
    length = math.sqrt(length)
    return length


initial_x = 10
initial_y = 10
next_x = input("The next x value ==> ")
next_y = input("The next y value ==> ")
total = line_length(initial_x, initial_y, next_x, next_y)

print("The line has moved from ({:d},{:d}) ".format(initial_x, initial_y) +
    "to (" + str(next_x) + ",", str(next_y) + ")")
print("Total length traveled is {:.2f}".format(total) )


