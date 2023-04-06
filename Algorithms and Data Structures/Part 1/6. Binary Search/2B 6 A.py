n = int(input())
a = list(map(int, input().split()))
k = int(input())

a.sort()
def checkl(m, params):
    a, b = params
    return a[m] >= b

def checkr(m, params):
    a, b = params
    return a[m] > b

def binarysearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m+1
    if not check(l, checkparams):
        return n
    return l

ans = []
for i in range(k):
    b1, b2 = map(int, input().split())
    ans.append(binarysearch(0, n - 1, checkr, (a, b2))-binarysearch(0, n - 1, checkl, (a, b1)))
    # print(binarysearch(0, n - 1, checkr, (a, b2)))
    # print(binarysearch(0, n - 1, checkl, (a, b1)))
print(*ans)
