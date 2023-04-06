from threading import stack_size
from sys import setrecursionlimit


setrecursionlimit(1000000)
stack_size(134217728)


def dfs(edges,node,colors,path):
    colors[node] = 1
    for child in edges.get(node,[]):
        if colors[child] == 1:
            colors[0] = 1
        elif colors[child] == 0:
            dfs(edges,child,colors,path)
    colors[node] = 2
    path.append(node)
    

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
    colors = [0] * (N+1)
    path = []
    for i in range(1,N+1):
        if colors[i] == 0:
            dfs(edges,i,colors,path)
        # color 0 with 1 if we find a loop 
        if colors[0] == 1:
            path = [-1]
            break
    print(*path[::-1])