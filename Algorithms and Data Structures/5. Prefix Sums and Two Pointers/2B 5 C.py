N, M = map(int, input().split())
X = [(idx+1, x) for idx, x in enumerate(list(map(int, input().split())))]
Y = [(idx+1, y) for idx, y in enumerate(list(map(int, input().split())))]

p = 0
X.sort(key = lambda x: -x[1])
Y.sort(key = lambda x: -x[1])
ind_X = 0
ind_Y = 0
ans = [0] * N

while ind_X < N:
    if X[ind_X][1] <= (Y[ind_Y][1]-1):
        ans[X[ind_X][0]-1] = Y[ind_Y][0]
        ind_X += 1
        ind_Y += 1
        p += 1
    else:
        ind_X += 1
print(p)
print(*ans)
