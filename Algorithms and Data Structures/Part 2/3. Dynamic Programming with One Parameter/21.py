N = int(input())
comb = [1,1,1,1]
for i in range(2,N):
    new_combinations = [comb[0]+comb[2], comb[0]+comb[2], comb[1]+comb[3], comb[1]]
    comb = new_combinations
if N == 1:
    print(2)
else:
    print(sum(comb))