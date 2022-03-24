from math import sin

segments = []


def f(x):
    return sin(x) * x ** 2


def search_min(a, b, delta, epsylon):
    assert delta < epsylon, 'Delta must be lower than epsylon'
    assert a < b, 'Incorrect input of interval'
    iterations = 0
    while b - a > epsylon:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta

        if f(a) > f(b):
            a = x1
        elif f(a) < f(b):
            b = x2
        else:
            a, b = x1, x2

        iterations += 1
        segments.append((b - a))
    return (a + b) / 2, iterations


def get_segments(a, b, d, e):
    search_min(a, b, d, e)
    return segments
