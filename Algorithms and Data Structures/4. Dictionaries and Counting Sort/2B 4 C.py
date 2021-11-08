words = {}
with open('input.txt', 'r') as file:
    for row in file:
        if len(row) == 1: break
        s_words = list(row.split())
        for word in s_words:
            words[word] = 1 if word not in words else words[word]+1
tuples = []
for key in words.keys():
    tuples.append((-words[key], key))
tuples.sort()
for tuple in tuples:
    print(tuple[1])
