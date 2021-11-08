m = int(input())
witnesses = []
for i in range(m):
    witnesses.append(input())
n = int(input())
plates = []
for i in range(n):
    plates.append(input())

max_counter = 0
suspects = []
for plate in plates:
    sp = set(plate)
    counter = 0
    for witness in witnesses:
        if set(witness).issubset(sp):
            counter += 1
    if counter > max_counter:
        suspects = [plate]
        max_counter = counter
    elif counter == max_counter:
        suspects.append(plate)
for suspect in suspects:
    print(suspect)
