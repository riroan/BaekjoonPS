from collections import defaultdict
n=int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
dd = defaultdict(set)
for i in range(n):
    for j in range(n):
        dd[arr[i]+arr[j]].add(i)
        dd[arr[i]+arr[j]].add(j)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if dd[arr[j] - arr[i]]:
            ans = max(ans, arr[j])
print(ans)