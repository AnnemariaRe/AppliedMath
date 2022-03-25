from math import *


def f(x):
    return sin(x) * x ** 2

def F(n):
    if n in {0, 1}: return n
    return 1 / sqrt(5) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n)


def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval (ಠ ͜ʖಠ)'
    iterations = 0
    oracle_calls = 0
    segments = []
    n = int((b - a) // eps)

    x1 = a + (F(n) / F(n + 2)) * (b - a)
    x2 = a + (F(n + 1) / F(n + 2)) * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    oracle_calls += 2

    while b - a > eps:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (F(n + 1) / F(n + 2)) * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (F(n) / F(n + 2)) * (b - a)
            f1 = f(x1)

        iterations += 1
        oracle_calls += 1
        segments.append((b - a))

    return [((a + b) / 2, iterations), oracle_calls, segments]

print(search_min(2, 7, 0.01))
