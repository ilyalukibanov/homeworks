with open('input.txt', 'r') as file:
    N = int(file.readline())
    a = list(map(int, file.readline().split()))
    M = int(file.readline())
    b = list(map(int, file.readline().split()))
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    i, j = N, M
    path = []
    while (i > 0) and (j > 0):
        if (dp[i-1][j] == dp[i][j]):
            i -= 1
        elif (dp[i][j-1] == dp[i][j]):
            j -= 1
        else:
            path.append(a[i-1])
            i -= 1
            j -= 1
    print(*path[::-1])