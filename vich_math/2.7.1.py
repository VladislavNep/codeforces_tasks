import math


def value_f(x, y):
    return round(math.sin(x+2.1) - 3*y + 0.4, 5)


def value_g(x, y):
    return round(math.cos(y+1.8) + 1.2*x, 5)


def value_fx(x):
    return round(math.cos(x+2.1), 5)


def value_gy(y):
    return round(-math.sin(y+1.8))


fy = -3
gx = -1.2


def newthon_system(x0, y0, eps=0.001):
    f = value_f(x0, y0)
    g = value_g(x0, y0)
    fx = value_fx(x0)
    gy = value_gy(y0)
    x1 = round(x0 + ((f*gy - fy*g)/(fx*gy - fy*gx)), 5)
    y1 = round(y0 + ((fx*g - f*gx)/(fx*gy - fy*gx)), 5)
    print(f"x: {x0}", f"f: {f}", f"fx: {fx}", f"fy: {fy}", f"h(x): {x1 - x0}")
    print(f"y: {y0}", f"g: {g}", f"gx: {gx}", f"gy: {gy}", f"h(y): {y1 - y0}")
    print()
    if abs(x1 - x0) <= eps and abs(y1 - y0) <= eps:
        return f'x = {x0} y = {y0}'

    return newthon_system(x0=x1, y0=y1)


print(newthon_system(x0=-0.8, y0=0.4))


