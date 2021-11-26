from itertools import combinations


string,n_combin = input(). split()
string = sorted(string)
comb = []
for x in range(1, int(n_combin)+1):
    combList = list(combinations(string,x))
    comb.append(combList)
    
for x in comb:
    # unire le tuple
    for y in x:
        print(''.join(y))


