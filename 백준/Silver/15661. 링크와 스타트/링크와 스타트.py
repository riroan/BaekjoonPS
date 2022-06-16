from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 987654321000
for ix in range(1,2**n-1):
    brr = []
    crr = []
    for i in range(n):
        if (1<<i)&ix:
            brr.append(i)
        else:
            crr.append(i)
    a,b=0,0
    for i in range(len(brr)):
        for j in range(len(brr)):
            a+=arr[brr[i]][brr[j]]
    for i in range(len(crr)):
        for j in range(len(crr)):
            b += arr[crr[i]][crr[j]]
    ans = min(ans, abs(a-b))
print(ans)