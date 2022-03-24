from math import sin


def f(x):
    return sin(x) * x ** 2


def search_min(a, c, epsylon):
    segments = []
    assert a < c, 'Incorrect input of interval'
    iterations = 0
    oracle_calls = 0
    while c - a > epsylon:
        y1 = f(a)
        y3 = f(c)
        b = (c + a) / 2
        y2 = f(b)
        assert (2 * ((b - a) * (f(b) - f(c)) - (b - c) * (f(b) - f(a)))) != 0, 'Divide by zero :c'

        u = abs(b - (((b - a) ** 2) * ((y2 - y3) - ((b - c) ** 2) * (y3 - y1))
                     / (2 * ((b - a) * (y2 - y3) - (b - c) * (y2 - y1)))))
        fu = f(u)
        oracle_calls += 4
        if b < u:
            if y2 < fu:
                c = u
            else:
                a = b
        else:
            if y2 < fu:
                a = u
            else:
                c = b

        iterations += 1
        segments.append(c - a)

    return [((c + a) / 2, iterations), oracle_calls, segments]

