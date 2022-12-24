# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:36:13 2021

@author: Oscar
"""

def get_line(fname, para, line):
    f = open(fname+'.txt')
    parals = (f.read()).split('\n\n')
    linels = parals[para].strip().split('\n')
    
    return (linels[line])

def parse_line(txt):
    ls = (txt.split('/'))
    if ls[-1].isnumeric() and ls[-2].isnumeric() and ls[-3].isnumeric():
        finls.append(ls[-3])
        finls.append(int(ls[-2]))
        finls.append(int(ls[-1]))
        finls.append(ls[0]+'/'+(ls[1]))
        return (finls)
    else:
        return ('None')
        
fname = input('File Name: ')
print (fname)
para = int(input("Paragraph: "))
print (para)
line = int(input("Line: "))
print (line)
get_line(fname, para-1, line-1)
print ('{0}/{1}/{2}'.format(fname, para, line))
while True:
    finls = []
    finls = parse_line(str(get_line(fname, para-1, line-1)))
    fname = finls[0]
    para = finls[1]
    line = finls[2]
    if fname == '0' or fname == 'N':
        print ("END/0/0/0")
        break
    print ('{0}/{1}/{2}'.format(fname, para, line))
    
    