a, k, b, m, x = list(map(int, input().split()))

def func_value(t):
    return (a + b) * t - a * (t // k) - b * (t // m)

def check_sign(t):
    return func_value(t) >= x

def binsearch(l, r, check):
    while l < r:
        m = (l+r) // 2
        if check(m):
            r = m
        else:
            l = m+1
    return l

print(binsearch(0, x, check_sign))

