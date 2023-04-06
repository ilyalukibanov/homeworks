import math

events = []
r_l, r_h = 0, 100001
n_drops = 0
starts = set()
ends = set()
with open('input.txt', 'r') as file:
    for i, row in enumerate(file):
        if i == 0: n = int(row)
        elif len(row) == 1: break
        else:
            r1, r2, phi1, phi2 = map(float, row.split())
            r_l = max(r_l, r1)
            r_h = min(r_h, r2)
            if phi1 < phi2:
                x = phi1 / (2 * math.pi)
                phi1 = (x - int(x)) * (2 * math.pi)
                x = phi2 / (2 * math.pi)
                phi2 = (x - int(x)) * (2 * math.pi)
                if phi1 not in starts or phi2 not in ends:
                    events.append((phi1, -1))
                    starts.add(phi1)
                    events.append((phi2, 1))
                    ends.add(phi2)
                else:
                    n_drops += 1
            else:
                x = phi1 / (2 * math.pi)
                phi1 = (x - int(x)) * (2 * math.pi)
                x = phi2 / (2 * math.pi)
                phi2 = (x - int(x)) * (2 * math.pi)
                if phi1 not in starts or phi2 not in ends:
                    events.append((phi1, -1))
                    starts.add(phi1)
                    events.append((2*math.pi, 1))
                    ends.add(2*math.pi)
                    events.append((0.00000001, -1))
                    starts.add(0.00000001)
                    events.append((phi2, 1))
                    ends.add(phi2)
                else:
                    n_drops += 1
events.sort()

r = r_h ** 2 - r_l ** 2
phi1 = 0
phi2 = 0
counter = 0
area = 0

for event in events:
    if event[1] == -1:
        counter += 1
    elif counter == (n-n_drops) and event[1] == 1:
        phi2 = event[0]
        area += (phi2 - phi1) / 2 * r
        counter -= 1
    else:
        counter -= 1
    if counter == (n-n_drops):
        phi1 = event[0]
print(area)

