from math import sin


def f(x):
    return sin(x) * x ** 2


def search_min(a, b, delta, epsylon):
    assert delta < epsylon, 'Delta must be lower than epsylon'
    assert a < b, 'Incorrect input of interval'
    iterations = 0
    oracle_calls = 0
    segments = []

    while b - a > epsylon:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta

        fa = f(a)
        fb = f(b)

        oracle_calls += 2

        if fa > fb:
            a = x1
        elif fa < fb:
            b = x2
        else:
            a, b = x1, x2

        iterations += 1
        segments.append((b - a))
    return [((a + b) / 2, iterations), oracle_calls, segments]
