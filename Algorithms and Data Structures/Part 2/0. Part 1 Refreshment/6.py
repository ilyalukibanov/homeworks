with open('input.txt', 'r') as file:
    all_systems = []
    active_systems = set()
    for i, line in enumerate(file):
        if i == 0:
            M = int(line)
        elif i == 1:
            N = int(line)
        else:
            a, b = map(int, line.split())
            systems_to_remove = []
            for system in active_systems:
                if (((a <= all_systems[system][1]) and (b >= all_systems[system][1])) or
                    ((a <= all_systems[system][0]) and (b >= all_systems[system][0])) or 
                    ((a >= all_systems[system][0]) and (b <= all_systems[system][1]))):
                    systems_to_remove.append(system)
            for system in systems_to_remove:
                active_systems.remove(system)
            system_number = i-2
            active_systems.update([system_number])
            all_systems.append((a, b))
print(len(active_systems))