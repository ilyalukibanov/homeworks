S = int(input())
A = [(ind-1, x) for ind, x in enumerate(list(map(int, input().split())))]
nA = A.pop(0)[1]
B = [(ind-1, x) for ind, x in enumerate(list(map(int, input().split())))]
nB = B.pop(0)[1]
C = [(ind-1, x) for ind, x in enumerate(list(map(int, input().split())))]
nC = C.pop(0)[1]
A.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[1])
C.sort(key=lambda x: x[1])
ans = []
min_ind = nA

for i in range(nA):
    l = 0
    r = nC-1
    D = S-A[i][1]
    if len(ans) == 0 or A[i][0] < min_ind:
        for j in range(nB+nC):
            # print(r)
            # print(l)
            if l == (nB-1):
                if B[l][1] + C[r][1] == D:
                    ans.append((A[i][0], B[l][0], C[r][0]))
                    min_ind = A[i][0]
                r -= 1
            elif r == 0:
                if B[l][1] + C[r][1] == D:
                    ans.append((A[i][0], B[l][0], C[r][0]))
                    min_ind = A[i][0]
                l += 1
            else:
                if B[l][1] + C[r][1] == D:
                    ans.append((A[i][0], B[l][0], C[r][0]))
                    min_ind = A[i][0]
                    r -= 1
                elif B[l][1] + C[r][1] > D:
                    r -= 1
                else:
                    l += 1
ans.sort()
if len(ans) == 0: print(-1)
else: print(*ans[0])
