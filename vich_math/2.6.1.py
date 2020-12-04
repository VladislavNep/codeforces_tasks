import math


def f_1(y):
    return math.cos(y+1)/2


def df_1(y):
    return -math.sin(y+1)/2


def f_2(x):
    return 0.4 - math.sin(x)


def df_2(x):
    return -math.cos(x)


def picar(x0, y0, eps=0.001):
    dfx_0 = df_1(y0)
    dfy_0 = df_2(x0)
    x1 = f_1(y0)
    y1 = f_2(x0)
    dfx_1 = df_1(y1)
    dfy_1 = df_2(x1)
    print(f"x: {x0}", f"y: {y0}", f"f'1(y): {dfx_0}", f"f'2(x): {dfy_0}")
    if abs(dfx_1 - dfx_0) <= eps and abs(dfy_1 - dfy_0) <= eps:
        return f'x = {x0} y = {y0}'

    return picar(x0=x1, y0=y1)


print(picar(x0=0.3, y0=0.3))


