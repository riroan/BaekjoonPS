n, k = map(int, input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(2**k):
    t = 0
    for j in range(k):
        if i & (1<<j):
            t+= arr[j]
    if t <= n:
        ans = max(ans,  t)
print(ans)