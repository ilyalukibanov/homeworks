n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

def func_value(length):
    counter = 1
    start = 0
    for i in range(1, n):
        if x[i] > length + x[start]:
            start = i
            counter += 1
    #print(counter)
    return counter

def check(length):
    return func_value(length) <= k

def binsearch(l, r, check):
    while l < r:
        m = (l+r) // 2
        if check(m):
            r = m
        else:
            l = m+1
        #print(m)
    return l
if n == k:
    print(0)
else:
    print(binsearch(0, max(x)-min(x), check))

