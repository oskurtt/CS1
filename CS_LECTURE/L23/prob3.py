
def fib(n):
    if n == 0 or n ==1:
        return n
    else:
        x = 0
        y = 1
        for i in range(n):
            x = y - x
            y += x
        return x 
if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
