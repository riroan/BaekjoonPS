n, k = map(int, input().split())
arr = [int(input()) for i in range(k)]
ans = 10**18
for i in range(2**k):
    t = 0
    for j in range(k):
        if i & (1<<j):
            t+= arr[j]
    if t >= n:
        ans = min(ans,  t)
print(ans)