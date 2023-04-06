candidates = {}
with open('input.txt', 'r') as file:
    for row in file:
        if len(row) == 1: break
        candidate, votes = row.split()
        votes = int(votes)
        candidates[candidate] = votes if candidate not in candidates else candidates[candidate]+votes
for key in sorted(candidates.keys()):
    print(key, candidates[key])
