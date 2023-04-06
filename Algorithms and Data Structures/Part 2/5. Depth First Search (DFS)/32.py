with open('input.txt', 'r') as file:
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
    components = []
    to_traverse_all = set(range(1,N+1))
    while to_traverse_all:
        to_traverse = set([to_traverse_all.pop()])
        component = set()
        while to_traverse:
            current_edge = to_traverse.pop()
            if current_edge in component:
                pass
            else:
                component.update([current_edge])
                if current_edge in edges:
                    for edge in edges[current_edge]:
                        to_traverse.update([edge])
                        if edge in to_traverse_all:
                            to_traverse_all.remove(edge)
        components.append(component)
print(len(components))
for component in components:
    print(len(component))
    print(*component)