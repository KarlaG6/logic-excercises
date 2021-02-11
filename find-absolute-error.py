import math

def func_expo(x, n):
    func = i = 0
    while i < n:
        func += x**i/math.factorial(i)
        i += 1
    return func

func_expo(0.5, 3)

def find_error_ab(m, l):
    r = 0
    r =( m - l )*100/m
    print(r)
    return r

find_error_ab(func_expo(0.5, 3), func_expo(0.5, 2))
