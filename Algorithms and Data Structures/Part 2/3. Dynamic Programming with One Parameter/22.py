with open('input.txt', 'r') as file:
    N, k = map(int, file.readline().split())
    if N == 1:
        dp = [1]
    else:
        dp = [0] * (N-1)
        for i in range(0, min(N-1,k)):
            dp[i] += 1
            for j in range(i):
                dp[i] += dp[j]
        for i in range(k, N-1):
            for j in range(i-k,i):
                dp[i] += dp[j]
    print(dp[-1])