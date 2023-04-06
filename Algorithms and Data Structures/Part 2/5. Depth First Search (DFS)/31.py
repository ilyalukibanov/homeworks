with open('input.txt', 'r') as file:
    from collections import deque
    N, M = map(int, file.readline().split())
    edges = {}
    to_traverse = deque()
    for i in range(M):
        f, s = map(int, file.readline().split())
        if f == 1: 
            to_traverse.append(s)
        elif s == 1:
            to_traverse.append(f)
        else:
            if f in edges:
                edges[f].append(s)
            else:
                edges[f] = [s]
            if s in edges:
                edges[s].append(f)
            else:
                edges[s] = [f]
    traversed = set([1])
    while to_traverse:
        current_edge = to_traverse.pop()
        if current_edge in traversed:
            pass
        else:
            traversed.update([current_edge])
            for edge in edges[current_edge]:
                if edge not in traversed:
                    to_traverse.append(edge)
    traversed = list(traversed)
    traversed.sort()
    print(len(traversed))
    print(*traversed)