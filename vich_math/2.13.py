from sympy.codegen.tests.test_applications import np


def simpson_method(f, a, b, n=50):
    if n % 2 == 1:
        raise ValueError("n must be an even integer.")
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    res = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return res


print(simpson_method(lambda x: x ** 2 * np.log10(x), 1.4, 3.0, 50))
# 2.9899609635777256
