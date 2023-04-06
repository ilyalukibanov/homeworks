with open('input.txt', 'r') as file:
    from collections import deque
    N, M = map(int, file.readline().split())
    edges = {}
    for i in range(M):
        f, s = map(int, file.readline().split())
        if f in edges:
            edges[f].append(s)
        else:
            edges[f] = [s]
        if s in edges:
            edges[s].append(f)
        else:
            edges[s] = [f]
    colors = [0] * (N+1)
    is_visited = [False] * (N+1)
    to_traverse = set(range(1,N+1))
    is_bipartite = True
    while to_traverse:
        stack = deque()
        random_node = to_traverse.pop()
        colors[random_node] = 1
        stack.append(random_node)
        while stack and is_bipartite:
            current_node = stack.pop()
            if current_node in edges:
                for neighbor in edges[current_node]:
                    if colors[neighbor]:
                        if colors[current_node] == colors[neighbor]:
                            is_bipartite = False
                            break
                    else:
                        stack.append(neighbor)
                        colors[neighbor] = 3-colors[current_node]
                is_visited[current_node] = True
                if current_node in to_traverse:
                    to_traverse.remove(current_node)
    if is_bipartite:
        print('YES')
    else:
        print('NO')
