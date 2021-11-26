from itertools import permutations

string,n_permutation = input().split()
permutation = ["".join(i) for i in permutations(string,int(n_permutation))]
permutation.sort()
print("\n".join(permutation))
