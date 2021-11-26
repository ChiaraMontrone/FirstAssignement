n, m = input().split()
integer_value = (input().split())
A = set(input().split())
B = set(input().split())

happyness = 0
for item in integer_value:
    if item in A:
        happyness = happyness + 1
    if item in B:
        happyness = happyness - 1
print (happyness)
 



