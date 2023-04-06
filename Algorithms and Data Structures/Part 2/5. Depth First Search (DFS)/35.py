from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit(1000000)
stack_size(134217728)


def dfs(edges,node,parent,colors,loop):
    colors[node] = 1
    for child in edges.get(node,[]):
        # print(node, child, parent)
        if colors[0]:
            break
        if (colors[child] == 1) and child != parent:
            colors[0] = 1
            colors[-1] = child
        elif colors[child] == 0:
            dfs(edges,child,node,colors,loop)
    # print(colors)
    if colors[0] == 1:
        loop.append(node)
    if node == colors[-1]:
        colors[0] = 2
        return
    if colors[0] == 2:
        return
    else:
        colors[node] = 2


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
    # 0 - flag for loop 
    # -1 element - index of loop start
    colors = [0] * (N+2)
    loop = []
    # print(edges)
    for i in range(1,N+1):
        if colors[i] == 0:
            dfs(edges,i,0,colors,loop)
        if colors[0] == 2:
            break
    if loop:
        print('YES')
        print(len(loop))
        print(*loop)
    else:
        print('NO')