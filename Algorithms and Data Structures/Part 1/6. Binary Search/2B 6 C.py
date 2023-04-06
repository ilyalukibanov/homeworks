import math
a, b, c, d = list(map(int, input().split()))

def func_value(x):
    return a * x ** 3 + b * x ** 2 + c * x + d

def check_sign_pos(x):
    return func_value(x) > 0

def check_sign_neg(x):
    return func_value(x) < 0

def fbinsearch(l, r, eps, check):
    while l + eps < r:
        m = l + (r-l) / 2
        if check(m):
            r = m
        else:
            l = m
        #print(l)
    return l

eps = 0.0000001
if func_value(-2 ** 64) < 0:
    print(format(fbinsearch(-2 ** 64, 2 ** 64, eps, check_sign_pos), '.10f'))
else:
    print(format(fbinsearch(-2 ** 64, 2 ** 64, eps, check_sign_neg), '.10f'))
