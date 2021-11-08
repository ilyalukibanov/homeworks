N, i, j = map(int, input().split())
if j < i: i, j = j, i
a = j - i - 1
b = (N+i-1) - j
print(min(a,b))
