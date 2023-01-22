import numpy as np


def q1():
    N_STR = '010000000111111010111001'

    s, e, m = N_STR[:1], N_STR[1:12], N_STR[12:]

    s = (-1)**(int(s))  # Sign
    e = int(e, 2)  # Exponent (of 2)
    m = sum(int(m[i]) * 2**(-i) for i in range(len(m)))  # Mantissa

    return s * m * 2**(e - 1023)


# This function is utterly incomplete but it works
# as long as you don't feed it a weird value for k
def chop(n, k):
    # Determine magnitude of n to restore after truncation
    d = 0
    while abs(n) >= 1:
        d += 1
        n /= 10

    return np.trunc(n * 10**k) * 10**(d - k)


def q2():
    ans = q1()
    return chop(ans, 3)


# This one sucks too for the same reasons
def round(n, k):
    d = 0
    while n >= 1:
        d += 1
        n /= 10

    # Add 0.5 to round
    sigma = 10**-6  # Combat round-off error when adding 0.5
    return np.trunc(n * 10**k + 0.5 + sigma) * 10**(d - k)


def q3():
    ans = q1()
    return round(ans, 3)


def q4():
    p_approx = q3()
    p = q1()

    err_abs = abs(p - p_approx)
    err_rel = abs(p - p_approx) / abs(p)

    return err_abs, err_rel


def q5():
    def summand(k):
        return 1 / k**3

    tol = 10**-4

    k = 1
    while summand(k) >= tol:
        k += 1

    return k + 1


def bisection(a, b, f, tol):
    def same_sign(a, b):
        return a * b >= 0

    i = 0
    while abs(b - a) > tol:
        i += 1
        mid = (a + b) / 2

        if not same_sign(f(a), f(mid)):
            b = mid
        else:
            a = mid

    return i


def newton(p, f, df, tol):
    i = 0
    while True:
        if df(p) != 0:
            p_next = p - f(p) / df(p)

            if abs(p_next - p) < tol:
                print(p_next)
                return i

            i += 1
            p = p_next
        else:
            return -1


def q6():
    def f(x):
        return ((x + 4) * x) * x - 10

    def df(x):
        return (3 * x + 8) * x

    tol = 10**-4

    a, b = -4, 7

    bisect_iter = bisection(a, b, f, tol)
    newton_iter = newton(b, f, df, tol)

    return bisect_iter, newton_iter


if __name__ == '__main__':
    print(q1(), end='\n\n')
    print(q2(), end='\n\n')
    print(q3(), end='\n\n')
    print(*q4(), sep='\n', end='\n\n')
    print(q5(), end='\n\n')
    print(*q6(), sep='\n')