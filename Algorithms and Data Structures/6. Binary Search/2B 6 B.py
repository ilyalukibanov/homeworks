n = int(input())
a = list(map(int, input().split()))
k = int(input())
q = list(map(int, input().split()))

def checkl(m, params):
    a, b = params
    return a[m] >= b

def checkr(m, params):
    a, b = params
    return a[m] <= b

def lbinarysearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m+1
    if (checkparams[0][l] != checkparams[1]):
        return 0
    return l+1

def rbinarysearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    # print(l, checkparams[1])
    # print(check(l, checkparams))
    if (checkparams[0][l] != checkparams[1]):
        return 0
    return l+1

boundaries = {}
for element in set(q):
    boundaries[element] = (lbinarysearch(0, n - 1, checkl, (a, element)), rbinarysearch(0, n - 1, checkr, (a, element)))

for i in range(k):
    # print(q[i])
    print(*boundaries[q[i]])
