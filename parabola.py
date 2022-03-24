from math import sin

segments = []


def f(x):
    return sin(x) * x ** 2


def search_min(a, c, epsylon):
    assert a < c, 'Incorrect input of interval'
    iterations = 0

    while c - a > epsylon:
        y1 = f(a)
        y3 = f(c)
        b = (c + a) / 2
        y2 = f(b)
        assert (2 * ((b - a) * (f(b) - f(c)) - (b - c) * (f(b) - f(a)))) != 0, 'Divide by zero :c'

        u = abs(b - (((b - a) ** 2) * ((y2 - y3) - ((b - c) ** 2) * (y3 - y1))
                     / (2 * ((b - a) * (y2 - y3) - (b - c) * (y2 - y1)))))

        if b < u:
            if y2 < f(u):
                c = u
            else:
                a = b
        else:
            if y2 < f(u):
                a = u
            else:
                c = b

        iterations += 1
        segments.append(c - a)

    return (c + a) / 2, iterations


def get_segments(a, b, e):
    search_min(a, b, e)
    return segments
