with open('input.txt', 'r') as file:
    from collections import deque
    N, M, S, T, Q = map(int, file.readline().split())
    # 0, 1, -1, -2 - frames
    distances = [[-1] * (M+4) for _ in range(N+4)]
    is_visited = [[False] * (M+4) for _ in range(N+4)]
    for i in [0,1,-1,-2]:
        for j in range(M+4):
            is_visited[i][j] = True
    for i in range(N+4):
        for j in [0,1,-1,-2]:
            is_visited[i][j] = True
    moves = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
    to_traverse = deque()
    to_traverse.append((S+1,T+1,0))
    is_visited[S+1][T+1] = True
    distances[S+1][T+1] = 0
    while to_traverse:
        cx, cy, cd = to_traverse.pop()
        for dx, dy in moves:
            if not is_visited[cx+dx][cy+dy]:
                nx, ny = cx+dx, cy+dy
                is_visited[nx][ny] = True
                distances[nx][ny] = cd+1
                to_traverse.appendleft((cx+dx, cy+dy, cd+1))
    length = 0
    for _ in range(Q):
        i, j = map(int, file.readline().split())
        if distances[i+1][j+1] == -1:
            length = -1
            break
        else:
            length += distances[i+1][j+1]
    print(length)