n = int(input())
arr= []
for a in range(0,n):
    x,s = input().split()
    arr.append(int(x))

out = [0]*(100)
count=0
for b in range (0, len(out)):
    for y in range (0, len(arr)):
        if arr[y] == b:
            count +=1
    out[b]= count
    
print(' '.join(str(x) for x in out))
            

    
