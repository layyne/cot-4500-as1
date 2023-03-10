import numpy as np
from numpy.polynomial import Polynomial
from decimal import Decimal


# Question 1
def q1():
    N_STR = '010000000111111010111001'

    s, e, m = N_STR[:1], N_STR[1:12], N_STR[12:]

    s = (-1)**(int(s))  # Sign
    e = 2**(int(e, 2) - 1023)  # Exponent
    m = 1 + sum(int(m[i]) * 2**(-(i+1)) for i in range(len(m)))  # Mantissa

    return s * m * e


# This function is utterly incomplete but it works
# as long as you don't feed it a weird value for k
def chop(n: float, k: int):
    # Determine digit count of n to restore after truncation
    d = 0
    while abs(n) >= 1:
        d += 1
        n /= 10

    return np.trunc(n * 10**k) * 10**(d - k)


# Question 2
def q2():
    ans = q1()
    return chop(ans, 3)


# This one sucks too for the same reasons
def round(n: float, k: int):
    d = 0
    while n >= 1:
        d += 1
        n /= 10

    # Add 0.5 to round
    sigma = 10**-6  # Combat round-off error when adding 0.5
    return np.trunc(n * 10**k + 0.5 + sigma) * 10**(d - k)


# Question 3
def q3():
    ans = q1()
    return round(ans, 3)


# Question 4 (two answers)
def q4():
    # I wasn't getting accurate results without using this class
    p_approx = Decimal(q3())
    p = Decimal(q1())

    err_abs = abs(p - p_approx)  # Absolute error
    err_rel = err_abs / abs(p)  # Relative error

    return err_abs, err_rel


# Question 5
def q5():
    # We can ignore the alternation, and x**k will always be 1
    def summand(k):
        return 1 / k**3

    tol = 10**-4

    k = 1
    while summand(k) > tol:
        k += 1

    # Partial sum up to a_{n-1} has error <= a_n
    return k - 1


# Returns the minimum number of steps it takes the root-finding bisection method
# to find a root of f within a certain error (tol), starting with bounds a and b
def bisection(a: float, b: float, f: Polynomial, tol: float):
    def same_sign(a, b):
        return a * b > 0

    i = 0
    while abs(b - a) > tol:
        i += 1
        mid = (a + b) / 2

        if not same_sign(f(a), f(mid)):
            b = mid
        else:
            a = mid

    return i


# Returns the minimum number of steps it takes Newton's root-finding method to
# find a root of f within a certain error (tol), starting with initial guess p
def newton(p: float, f: Polynomial, tol: float):
    df = f.deriv()
    i = 0
    while True:
        if df(p) == 0:
            return -1

        p_next = p - f(p) / df(p)

        if abs(p_next - p) < tol:
            return i + 1

        i += 1
        p = p_next


# Question 6 (two answers)
def q6():
    coef = [-10, 0, 4, 1]
    f = Polynomial(coef)

    a, b = -4, 7
    tol = 10**-4

    bisect_iter = bisection(a, b, f, tol)
    newton_iter = newton(b, f, tol)

    return bisect_iter, newton_iter


if __name__ == '__main__':
    print(q1(), end='\n\n')

    print(q2(), end='\n\n')

    print(q3(), end='\n\n')

    err_abs, err_rel = q4()
    print(err_abs)
    print(f'{err_rel:.31f}', end='\n\n')

    print(q5(), end='\n\n')

    print(*q6(), sep='\n\n')
