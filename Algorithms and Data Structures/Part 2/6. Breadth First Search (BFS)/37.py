with open('input.txt', 'r') as file:
    from collections import deque
    N = int(file.readline())
    edges = {}
    for i in range(1, N+1):
        for j, is_connected in enumerate(list(map(int, file.readline().split()))):
            if is_connected:
                if i in edges:
                    edges[i].append(j+1)
                else:
                    edges[i] = [j+1]
    start, end = map(int, file.readline().split())
    prev = [-1] * (N+1)
    prev[start] = -2
    to_traverse = deque()
    to_traverse.append((start,1))
    is_reacheble = False
    shortest_length = -1
    if start == end:
        is_reacheble = True
        shortest_length = 0
    while to_traverse and not is_reacheble:
        current_node, current_depth = to_traverse.pop()
        for neighbor in edges.get(current_node, []):
            if neighbor == end:
                is_reacheble = True
                shortest_length = current_depth
                prev[neighbor] = current_node
                break
            elif prev[neighbor] == -1:
                to_traverse.appendleft([neighbor,current_depth+1])
                prev[neighbor] = current_node
    print(shortest_length)
    if shortest_length > 0:
        path = []
        current_node = end
        while current_node != -2:
            path.append(current_node)
            current_node = prev[current_node]
        print(*path[::-1])