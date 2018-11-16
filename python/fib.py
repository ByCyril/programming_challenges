# Programmer: Cyril Garcia
# Date: November 10, 2018

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



a = fib(2)
b = fib(4)
c = fib(7)
d = fib(8)
print(a,b,c,d)