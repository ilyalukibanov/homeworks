import copy

def find_terminal_nodes(node):
    terminal_nodes = []
    path = []
    to_visit = []
    if len(connections[node]) == 1:
        terminal_nodes.append(node)
    for child in connections[node]:
        if child not in path:
            to_visit.append(child)
    while to_visit:
        path.append(node)
        node = to_visit.pop(-1)
        for child in connections[node]:
            if child not in path:
                to_visit.append(child)
        if len(connections[node]) == 1:
            terminal_nodes.append(node)
    return terminal_nodes

def search(key, path, weight=0):
    weight += weights[key]
    path.append(key)
    for child in connections[key]:
        local_nodes.add(child)
        #print(len(path), path, child)
        if len(connections[child]) == 1:
            sizes.append((weight+weights[child], child))
        elif child not in path:
            search(child, path.copy(), weight)

def reduce_tree():
    for element in terminal_nodes:
        weight = 0
        if len(connections[connections[element][0]]) == 2:
            last_child, child = connections[element][-1], connections[element][-1]
            if len(connections[child]) == 2:
                connections[child].remove(element)
                while len(connections[child]) == 1:
                    connections[connections[child][0]].remove(child)
                    last_child, child = child, connections[child][0]
                    weight += 1
                    connections.pop(last_child)
                connections[element] = [child]
                connections[child].append(element)
                weights[element] += weight



n = int(input())
connections = {}
for i in range(n-1):
    a, b = map(int, input().split())
    if a not in connections:
        connections[a] = [b]
    else:
        connections[a].append(b)
    if b not in connections:
        connections[b] = [a]
    else:
        connections[b].append(a)

weights = {}
for key in connections.keys():
    weights[key] = 1

max_sizes = []

while connections:
    node = next(iter(connections))
    terminal_nodes = find_terminal_nodes(node)
    reduce_tree()
    local_nodes = set()
    #print(connections)
    # visited_routes = dict.fromkeys(terminal_nodes)
    # print(visited_routes)
    key = terminal_nodes[0]
    sizes = []
    local_nodes.add(key)
    search(key, [])
    key = max(sizes)[1]
    sizes = []
    search(key, [])
    max_sizes.append(max(sizes)[0])
    for node in local_nodes:
        connections.pop(node)
    #print(local_nodes)

print(max(max_sizes))
