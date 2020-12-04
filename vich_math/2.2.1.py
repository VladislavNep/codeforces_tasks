import math


def value_in_point(var):
    """
    Вычисление значения в точке
    :param var: float
    :return: value: float
    """
    return round(8 * math.sin(6.18 * var) - (6.25 * var), 3)


def gold_section(a, b, eps):
    """
    Вычисление корня уравнения методом бисекци.
    fa,fc,fb - значения функций в точке.
    :param a: начало интервала
    :param b: конец интервала
    :param eps: точность, задаётся пользователем
    :return: result
    """
    global c

    while math.fabs(b - a) >= eps:
        c = round(a + 0.3819660112501051 * (b - a), 6)
        fc = value_in_point(c)
        fa = value_in_point(a)

        print(f'a: {a}', f'b: {b}', f'c: {c}', f'fa*fc: { round(fa * fc, 6) }',
              f'|b-a|: {round(math.fabs(b - a), 6)}', f'fc: {fc}')

        # если нет пересечения с осью Х, то передвигаем левый конец интервала
        # в точку полуинтервала, иначе правый конец интервала передвигаем
        # в точку полуинтервала
        if fa * fc >= 0:
            a = c
        else:
            b = c

    else:
        return c


def go():
    eps = float(input("Введите eps(в виде 0.0...1): "))
    a, b = map(float, input("Введите интервал a и b через пробел: ").split())
    value = gold_section(a, b, eps)
    print(f'Корень уравнения: {value}')


if __name__ == '__main__':
    go()
