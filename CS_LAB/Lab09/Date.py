'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year = 1900, month = 1, day = 1):
        self.y  = year
        self.m = month
        self.d = day
    def __str__(self):
        sy = str(self.y)
        sm = str(self.m)
        sd = str(self.d)
        return ("{0}/{1}/{2}".format(sy, sm.rjust(2,'0'), sd.rjust(2,'0')))
    def same_day_in_year(self, self2):
        if (self.m == self2.m) and (self.d == self2.d):
            return True
        else:
            return False
    def is_leap_year(self):
        if ((self.y) %4 == 0) or (((self.y) %100 == 0) and ((self.y) %400 != 0)):
            return True
        else:
            return False
    def __lt__(self, self2):
        if self.y<self2.y:
            return True
        elif (self.y == self2.y) and (self.m<self2.m):
            return True
        elif (self.y == self2.y) and (self.m == self2.m) and (self.d < self2.d):
            return True
        else:
            return False
    pass


if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print (d1)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print (d1.is_leap_year())
    print (d2.is_leap_year())
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    print('')
    print (d1.__it__(d2))
    print (d2.__it__(d3))
    print (d3.__it__(d4))    
