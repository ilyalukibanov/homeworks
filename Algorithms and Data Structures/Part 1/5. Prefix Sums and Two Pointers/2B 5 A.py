n, q = map(int, input().split())
a = list(map(int, input().split()))
prefixes = [0] * (n+1)

for i in range(n):
    prefixes[i+1] = prefixes[i] + a[i]

for i in range(q):
    l, r = map(int, input().split())
    print(prefixes[r] - prefixes[l-1])
