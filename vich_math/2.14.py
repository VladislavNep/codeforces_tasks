from pylab import sum, np
from scipy.special.orthogonal import p_roots


def gauss(f, n, a, b):
    [x, w] = p_roots(n + 1)
    G = 0.5 * (b - a) * sum(w * f(0.5 * (b - a) * x + 0.5 * (b + a)))
    return G


print(gauss(lambda x: x/(np.sqrt((x**2)+2)), 50, 0.8, 2))
# 0.8246820618559857
