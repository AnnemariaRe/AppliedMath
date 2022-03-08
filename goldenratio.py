from math import sin
from math import *

ratio = (sqrt(5) - 1) / 2

def f(x):
    return sin(x) * x ** 2

def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval (ಠ ͜ʖಠ)'
    iter = 0

    while b - a > eps:
        d = ratio * (b - a)
        x1 = a + d
        x2 = b - d

        if f(x1) > f(x2):
            b = x1
        elif f(x1) < f(x2):
            a = x2
        else:
            a, b = x1, x2

        iter += 1

    return (a + b) / 2, iter

print(search_min(11, 16, 0.01))