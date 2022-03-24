from math import sin, sqrt

ratio = (sqrt(5) - 1) / 2

def f(x):
    return sin(x) * x ** 2

def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval (ಠ ͜ʖಠ)'

    iter = 0
    oracle_calls = 0

    while b - a > eps:
        d = ratio * (b - a)
        x1 = a + d
        x2 = b - d

        t = f(x1)
        k = f(x2)

        if t > k:
            b = x1
        elif t < k:
            a = x2
        else:
            a, b = x1, x2

        iter += 1
        oracle_calls += 2;

    return [(a + b) / 2, iter, oracle_calls]