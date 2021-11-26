from itertools import combinations_with_replacement

string,repetition = input().split()

string = sorted(string)
for i in list(combinations_with_replacement(string,int(repetition))):

    print(''.join(i))
    
