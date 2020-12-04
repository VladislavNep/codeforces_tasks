from sympy import diff, symbols, cos, sin, pi

# вычисляем производную
x_dif = symbols('x')
expr = diff((2.67*sin(3.044*x_dif))/2.25, x_dif)
# result: 3.61221 * cos(3.044*x)


# рекурсивный подход
def avd(x, eps=0.0001, k=0):
    # вычисление X(k+1)
    x1 = round(3.61221 * cos(3.044*x), 6)
    k += 1
    res = round(abs(x1 - (3.61221 * cos(3.044*x))), 10)
    print(f'k: {k}', f'корень: {x1}', f'abs: {res}')

    if res < eps:
        return x1

    return avd(x=x1, k=k)


print(f"Корень уравнения: {avd(x=pi * -0.3)}")
