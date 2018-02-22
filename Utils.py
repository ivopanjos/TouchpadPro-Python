from math import atan2, pi


def delta(a, b):
    return a - b


def average(a, b):
    return (a + b) / 2.0


def angle(x, y):
    return atan2(y, x) * 180.0 / pi

