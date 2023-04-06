N = 0
matrix = []
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            N, M, K = map(int, line.split())
            prefix_matrix = [[0]*(M+1) for _ in range(N+1)]
        elif (i < N):
            row = list(map(int, line.split()))
            matrix.append(row)
        elif (i == N):
            row = list(map(int, line.split()))
            matrix.append(row)
            for j in range(1, N+1):
                for k in range(1, M+1):
                    prefix_matrix[j][k] = prefix_matrix[j-1][k] + prefix_matrix[j][k-1] - prefix_matrix[j-1][k-1] + matrix[j-1][k-1]
        else:
            x1, y1, x2, y2 = map(int, line.split())
            result = prefix_matrix[x2][y2] - prefix_matrix[x2][y1-1] - prefix_matrix[x1-1][y2] + prefix_matrix[x1-1][y1-1]
            print(result)