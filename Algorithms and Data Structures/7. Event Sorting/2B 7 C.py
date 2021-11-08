m = int(input())
events = []
i = 0
while True:
    l, r = map(int, input().split())
    if l <= m and r >= 0:
        events.append((l, -1, r-l))
        events.append((r, 1))
    if l == r == 0: break
    i += 1
events.sort()

def find_n_segments(events):
    n_segments = 0
    segments = []
    current_right = 0
    next_right = 0
    n_open_intervals = 0
    i = 0
    ind_next_right = 0
    while i < len(events) and events[i][0] <= 0:
        if events[i][1] == -1:
            n_open_intervals += 1
            potential_right = events[i][0] + events[i][2]
            if current_right < potential_right:
                current_right = potential_right
                ind_next_right = i
        else:
            n_open_intervals -= 1
        i += 1
    segments.append([events[ind_next_right][0], events[ind_next_right][0]+events[ind_next_right][2]])
    n_segments += 1
    for j in range(i, len(events)):
        #print(events[j], current_right, next_right)
        if events[j][1] == -1:
            n_open_intervals += 1
            if events[j][0] > current_right:
                current_right = next_right
                segments.append([events[ind_next_right][0], events[ind_next_right][0]+events[ind_next_right][2]])
                n_segments += 1
                if events[j][0] > segments[-1][1]:
                    return (-1, [])
            potential_right = events[j][0] + events[j][2]
            if next_right < potential_right:
                next_right = potential_right
                ind_next_right = j
        else:
            n_open_intervals -= 1
        if n_open_intervals == 0 and j < len(events)-1:
            return (-1, [])
        if next_right >= m:
            segments.append([events[ind_next_right][0], events[ind_next_right][0] + events[ind_next_right][2]])
            n_segments += 1
            return (n_segments, segments)
    if segments[-1][1] < m: return (-1, [])
    return (n_segments, segments)

result = find_n_segments(events)
if result[0] == -1 or result[1] == []:
    print('No solution')
else:
    print(result[0])
    for i in range(len(result[1])):
        print(*result[1][i])
