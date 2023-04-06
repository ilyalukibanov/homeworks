s = input()
counts = {}
n = len(s) - 1
for i, letter in enumerate(s):
    counts[letter] = counts.get(letter, 0) + (n-i+1)*(i+1)
for key in sorted(counts):
    print(f'{key}: {counts[key]}')