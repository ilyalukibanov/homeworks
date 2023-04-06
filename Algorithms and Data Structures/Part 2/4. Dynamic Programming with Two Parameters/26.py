with open('input.txt', 'r') as file:
    N, M = map(int, file.readline().split())
    costs = []
    for i in range(N):
        costs.append(list(map(int, file.readline().split())))
    accumulative_costs = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N+1):
        accumulative_costs[i][0] = float('inf')
    for i in range(M+1):
        accumulative_costs[0][i] = float('inf')
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1 and j == 1:
                accumulative_costs[i][j] = costs[i-1][j-1]
            else:
                accumulative_costs[i][j] = min(accumulative_costs[i-1][j], accumulative_costs[i][j-1]) + costs[i-1][j-1]
    print(accumulative_costs[N][M])