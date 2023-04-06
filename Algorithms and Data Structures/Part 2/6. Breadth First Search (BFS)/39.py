with open('input.txt', 'r') as file:
    from collections import deque
    N = int(file.readline())
    cave = [[[0] * (N+2) for i in range(N+2)] for j in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            cave[0][i][j] = -1
            cave[-1][i][j] = -1
            cave[i][0][j] = -1
            cave[i][-1][j] = -1
            cave[i][j][0] = -1
            cave[i][j][-1] = -1
    sx, sy, sz = 0, 0, 0
    for b in range(1,N+1):
        _ = file.readline()
        for i in range(1,N+1):
            line = file.readline()
            for j, symbol in enumerate(line):
                if symbol == '#':
                    cave[b][i][j+1] = -1
                elif symbol == 'S':
                    sx, sy, sz = b, i, j+1
                    cave[sx][sy][sz] = -2
    moves = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))
    to_traverse = deque()
    to_traverse.append((sx, sy, sz, 0))
    is_reached = False
    shortest_distance = 0
    if sx == 1:
        is_reached = True
    while to_traverse and not is_reached:
        cx, cy, cz, current_depth = to_traverse.pop()
        for dx,dy,dz in moves:
            nx, ny, nz = cx+dx, cy+dy, cz+dz
            if cave[nx][ny][nz] == 0:
                if nx == 1:
                    shortest_distance = current_depth+1
                    is_reached = True
                    break
                else:
                    cave[nx][ny][nz] = current_depth+1
                    to_traverse.appendleft((nx, ny, nz, current_depth+1))
    print(shortest_distance)