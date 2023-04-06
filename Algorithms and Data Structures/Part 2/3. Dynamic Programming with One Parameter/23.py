N = int(input())
dp = [1] * (N+1)
dp[1] = 0
dp_ind = [-1] * (N+1)
if N >= 2: dp_ind[2] = 1
if N >= 3: dp_ind[3] = 1 
if N > 3:
    for i in range(4,N+1):
        min_operations = N
        ind_i = -1
        if i % 3 == 0:
            if min_operations > dp[ind := (i // 3)]:
                min_operations = dp[ind]
                ind_i = ind
        if i % 2 == 0:
            if min_operations > dp[ind := (i // 2)]:
                min_operations = dp[ind]
                ind_i = ind
        if min_operations > dp[i-1]:
            min_operations = dp[i-1]
            ind_i = i-1
        dp[i] = min_operations + 1
        dp_ind[i] = ind_i
transformations = []
ind = N
while ind > -1:
    transformations.append(ind)
    ind = dp_ind[ind]
print(dp[-1])
print(*transformations[::-1])