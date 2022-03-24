from functools import cache
from math import *

def f(x):
    return sin(x) * x ** 2

@cache
def F(n):
    if n in {0, 1}: return n
    return 1/sqrt(5) * ( ((1+sqrt(5)) / 2)**n - ((1-sqrt(5)) / 2)**n )

def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval (ಠ ͜ʖಠ)'

    iter = 0
    oracle_calls = 0

    n = int((b - a) // eps)

    while b - a > eps:
        x1 = a + ( F(n) / F(n + 2) ) * (b - a)
        x2 = a + ( F(n + 1) / F(n + 2) ) * (b - a)

        if f(x1) < f(x2):
            b = x2
            x2 = x1
        elif f(x1) >= f(x2):
            a = x1
            x1 = x2
        
        iter += 1
        oracle_calls += 4;

    return [(a + b) / 2, iter, oracle_calls]