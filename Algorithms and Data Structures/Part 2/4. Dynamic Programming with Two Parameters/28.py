with open('input.txt', 'r') as file:
    N, M = map(int, file.readline().split())
    costs = []
    pathways = [[0] * (M+1) for _ in range(N+1)]
    pathways[1][1] = 1
    for i in range(2, N+1):
        for j in range(2, M+1):
            pathways[i][j] = pathways[i-1][j-2] + pathways[i-2][j-1]
    print(pathways[N][M])