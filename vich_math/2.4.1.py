import math


def value(var):
    return round((math.cos(var) / math.sin(var)) - var/3, 4)


def hord(a, b, eps=0.001):
    print(f'Интервал: [{a} ; {b}]', f'eps: {eps}')
    fa = value(a)
    fb = value(b)

    def value_c():
        return round(a - (fa * ((b - a) / (fb - fa))), 4)

    c0 = value_c()
    fc = value(c0)
    i = 1
    while math.fabs(fc) != 0:
        if fa*fc < 0:
            fa = fc
            a = c0
        else:
            fb = fc
            b = c0

        c1 = value_c()
        fc = value(c1)

        print(f'№:{i}', f'x/3: {round(a/3, 4)}', f'ctg(x): {round(math.cos(a) / math.sin(a), 4)}', f'h: {round(c1-c0, 4)}')
        i += 1

        if math.fabs(c1-c0) <= eps:
            return f'Корень Уравнения: {c1}'
        else:
            c0 = c1
    else:
        return f'Корень Уравнения: {c0}'


print("Уравнение: ctg(x)-x/3")
print(hord(a=1.0, b=1.4))
