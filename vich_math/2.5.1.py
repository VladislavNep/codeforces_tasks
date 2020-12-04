import math


def f(x):
    return 9.667*math.sin(7.176*x)-7.5*x


def df(x):
    return 69.370392*math.cos(7.176*x) - 7.5


def dx(f, x):
    return abs(0 - f(x))


def newtons_method(f, df, x0, eps=0.001):
    delta = dx(f, x0)
    while delta > eps:
        x0 = x0 - f(x0) / df(x0)
        delta = dx(f, x0)
        print(f'X: {round(x0, 5)}', f'f(x): {round(f(x0), 5)}',
              f"f'(x): {round(df(x0), 5)}", f"f(x)/f'(x): {round(delta, 5)}")
    else:
        return f'Корень уравнения: {round(x0, 4)}'


print(newtons_method(f, df, x0=-10))
