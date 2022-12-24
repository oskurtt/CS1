""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""

# def addone(x):
#     '''
#     addone(x) returns 1 more than
#     the value x passed in.

#     >>> addone(5)
#     6
#     >>> addone(0)
#     1
#     '''
#     return x+1

def closest1 (list):
    '''
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    '''
    ls = []
    ls2 = []
    for i in range(0,10):
        for j in range(i+1, len(list)):
            val = abs(list[i]-list[j])
            ls.append(list[i])
            ls.append(list[j])
            ls.append(val)
            ls2.append(val)
    ind = (ls.index(min(ls2)))
    return (ls[ind-2], ls[ind-1])
if __name__ == "__main__":
    
    print (closest1(list))
    pass
