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

def closest2 (list):
    ls = []
    dictionary = dict()
    if len(list) < 2:
        return (None, None)
    else:
        for i in range(len(sorted(list))-1):
            x = sorted(list)[i]
            y = sorted(list)[i+1]
            ls.append(y-x)
            dictionary[y-x] = (x,y)
        closest = ls[0]
        for j in range(1, len(ls)):
            closest = min(closest, ls[j])
        return dictionary[closest]
if __name__ == "__main__":
    list =  [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    print (closest2(list))
    pass
