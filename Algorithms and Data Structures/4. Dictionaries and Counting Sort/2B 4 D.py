parties = {}
i = 0
sum_votes = 0
with open('input.txt', 'r') as file:
    for row in file:
        if len(row) == 1: break
        s = list(row.split())
        party_name = ' '.join(s[:len(s)-1])
        parties[party_name] = (i, int(s[-1]))
        sum_votes += int(s[-1])
        i += 1
# print(parties)
tuples = []
first_div = sum_votes / 450
for key in parties.keys():
    tuples.append((parties[key][0], parties[key][1], key))
# print(tuples)

sub_sum = 0
tuples_remainder = []
for tuple in tuples:
    votes = int(tuple[1] // first_div)
    tuples_remainder.append((*tuple, votes, tuple[1] % first_div))
    sub_sum += votes

# print(tuples_remainder)

sub_sum = int(sub_sum)
# print(sub_sum)

if sub_sum < 450:
    final = []
    sorted_list = sorted(tuples_remainder, key=lambda x: (-x[4], -x[1]))
    # print(sorted_list)
    for i in range(450-sub_sum):
        final.append((*sorted_list[i], sorted_list[i][3]+1))
    # print(final)
    for i in range(450-sub_sum, len(tuples_remainder), 1):
        final.append((*sorted_list[i], sorted_list[i][3]))
    for tuple in sorted(final):
        print(tuple[2], tuple[5])
else:
    for tuple in sorted(tuples_remainder):
        print(tuple[2], tuple[3])
