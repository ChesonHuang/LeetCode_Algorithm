i = int(input())
h = sorted([int(x) for x in input().split()],reverse=True)
j = int(input())
w = [int(x) for x in input().split()]
ans =0
tmp = []
for x in range(j):
    for y in range(k,i):
        if (not y in tmp) and w[x]>=h[y]:
            ans +=1
            tmp.append(y)
            break
            
print(ans)