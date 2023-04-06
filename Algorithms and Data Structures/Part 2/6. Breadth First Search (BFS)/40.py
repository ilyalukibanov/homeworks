with open('input.txt', 'r') as file:
    from collections import deque
    N = int(file.readline())
    M = int(file.readline())
    stations = {i: list() for i in range(1,N+1)}
    lines = {i: list() for i in range(1,M+1)}
    for i in range(1,M+1):
        for s in list(map(int, file.readline().split()))[1:]:
            stations[s].append(i)
            lines[i].append(s)
    start, end = map(int, file.readline().split())
    to_traverse = deque()
    visited_stations = [False] * (N+1)
    visited_stations[start] = True
    visited = set()
    for line in stations[start]:
        to_traverse.append((line,0))
        visited.update([(line,start)])
    is_reacheble = False
    n_transitions = -1
    while to_traverse and not is_reacheble:
        current_line, transitions = to_traverse.pop()
        for station in lines[current_line]:
            if station == end:
                is_reacheble = True
                n_transitions = transitions
                break
            elif not visited_stations[station]:
                visited_stations[station] = True
                for line in stations[station]:
                    if (line,station) not in visited:        
                        to_traverse.appendleft((line,transitions+1))
                        visited.update([(line,station)])
    print(n_transitions)