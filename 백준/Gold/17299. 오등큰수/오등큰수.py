from collections import defaultdict
n=int(input())
arr = list(map(int, input().split()))
d = defaultdict(int)
for i in arr:
    d[i]+=1
s=[]
ans = [-1]*n
for i in range(n):
    while s:
        if d[s[-1][0]] >= d[arr[i]]:
            break
        x, ix = s.pop()
        ans[ix] = arr[i]
    s.append([arr[i], i])
print(*ans)