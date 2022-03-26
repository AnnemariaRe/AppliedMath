from math import sin, sqrt

ratio = (3 - sqrt(5)) / 2


def f(x):
    return sin(x) * x ** 2


def search_min(a, b, eps):
    assert a < b, 'Incorrect input of interval'

    segments = []

    iterations = 0
    oracle_calls = 0

    x1 = a + ratio * (b - a)
    x2 = b - ratio * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    oracle_calls += 2

    while b - a > eps:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - ratio * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + ratio * (b - a)
            f1 = f(x1)

        iterations += 1
        oracle_calls += 1
        segments.append((b - a))

    return [((a + b) / 2, iterations), oracle_calls, segments]

