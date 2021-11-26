from collections import Counter

int(input())
sizes = list(map(int,input().split()))
income = 0
shoes_shops = Counter(sizes)
for i in range(int(input())):
    n,i = list(map(int,input().split()))
    if shoes_shops[n]:
        income += i
        shoes_shops[n] -=1
print(income)
