n_symbols = dict()
with open('input.txt', 'r') as file:
    for s in file:
        for symbol in s:
            if (symbol != ' ') and (symbol != '\n'):
                n_symbols[symbol] = n_symbols.get(symbol, 0) + 1
letters = sorted(n_symbols)
switch_times = []
output_list = [' '] * len(letters)
max_frequency = 0
for letter_position, letter in enumerate(letters):
    max_frequency = max(max_frequency, n_symbols[letter]) 
    switch_times.append((n_symbols[letter], letter_position))
switch_times.sort(reverse=True)
pointer = 0
for i in range(max_frequency, 0, -1):
    if (pointer < len(letters)) and (switch_times[pointer][0] == i):
        while (pointer < len(letters)) and (switch_times[pointer][0] == i):
            output_list[switch_times[pointer][1]] = '#'
            pointer += 1
    print(''.join(output_list))
print(''.join(letters))