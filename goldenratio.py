from math import sin, sqrt

ratio = (sqrt(5) - 1) / 2


def f(x):
    return sin(x) * x ** 2


def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval (ಠ ͜ʖಠ)'
    iterations = 0
    segments = []
    oracle_calls = 0
    while b - a > eps:
        d = ratio * (b - a)
        x1 = a + d
        x2 = b - d
        fx1 = f(x1)
        fx2 = f(x2)
        oracle_calls += 2
        if fx1 > fx2:
            b = x1
        elif fx1 < fx2:
            a = x2
        else:
            a, b = x1, x2

        iterations += 1
        segments.append((b - a))

    return [((a + b) / 2, iterations), oracle_calls, segments]

