# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:51:56 2021

@author: Oscar
"""

bpop = int(input("Number of bunnies ==> "))
print (bpop)
fpop = int(input("Number of foxes ==> "))
print (fpop)

def bunniespop (bpop):
    ls = [0]
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    ls.append(bpop_next)
    return max(ls)
def foxpop (fpop):
    ls = [0]
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    ls.append(fpop_next) 
    return max(ls)


b = bunniespop(bpop)
f = foxpop(fpop)
print ("Year 1: {0} {1}".format(bpop, fpop))
print ("Year 2: {0} {1}".format(b, f))

bpop = b
fpop = f

b = bunniespop(bpop)
f = foxpop(fpop)
print ("Year 3: {0} {1}".format(b, f))

bpop = b
fpop = f

b = bunniespop(bpop)
f = foxpop(fpop)
print ("Year 4: {0} {1}".format(b, f))

bpop = b
fpop = f

b = bunniespop(bpop)
f = foxpop(fpop)
print ("Year 5: {0} {1}".format(b, f))