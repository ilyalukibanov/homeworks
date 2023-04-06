from pprint import pprint
with open('input.txt', 'r') as file:
    N = int(file.readline())
    if N == 0:
        print(0)
        print(0, 0)
    else:
        costs = []
        for i in range(N):
            costs.append(int(file.readline()))
        dp = [[float('inf')] * (N+2) for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(1, N+1):
            for j in range(N+1):
                if costs[i-1] > 100:
                    if j == 0:
                        dp[i][j] = min(dp[i-1][j]+costs[i-1], dp[i-1][j+1])    
                    else:
                        dp[i][j] = min(dp[i-1][j-1]+costs[i-1], dp[i-1][j+1])    
                else:
                    dp[i][j] = min(dp[i-1][j]+costs[i-1], dp[i-1][j+1])
        min_index = 0
        min_cost = float('inf')
        # Find the last day number of coupons and costs
        for i, val in enumerate(dp[-1]):
            if min_cost >= val:
                min_cost = val
                min_index = i
        days = []
        # Backtrack the days when the coupons were used
        j = min_index
        path_coupons = []
        for i in range(N,-1,-1):
            path_coupons.append(j)
            if costs[i-1] > 100:
                if dp[i][j] == dp[i-1][j+1]:
                    days.append(i)
                    j += 1
                elif dp[i][j] == (dp[i-1][j]+costs[i-1]):
                    pass
                else:
                    j -= 1
            else:
                if dp[i][j] == dp[i-1][j+1]:
                    days.append(i)
                    j += 1
        n_coupons = 0
        path_coupons = path_coupons[::-1]
        for i, nc in enumerate(path_coupons[1:]):
            if nc == (path_coupons[i]+1):
                n_coupons += 1
        print(min_cost)
        print(min_index, n_coupons-min_index)
        for day in days[::-1]:
            print(day)