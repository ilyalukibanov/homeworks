with open('input.txt', 'r') as file:
    N = int(file.readline())
    coordinates = list(map(int, file.readline().split()))
    coordinates.sort()
    distances = [0,0]
    distances.extend([coordinates[i] - coordinates[i-1] for i in range(1,N)]) 
    dp = [0] * (N+1)
    breaks = [0] * (N+1)
    dp[1] = float('inf')
    dp[2] = distances[2]
    if N > 2: dp[3] = distances[2] + distances[3]
    for i in range(4,N+1):
        if breaks[i-2] == 0:
            if dp[i-2] < dp[i-1]:
                dp[i] = dp[i-2] + distances[i]
                breaks[i] == 1
            else:
                dp[i] = dp[i-1] + distances[i]
        else:
            dp[i] = dp[i-1] + distances[i]
    print(dp[-1])