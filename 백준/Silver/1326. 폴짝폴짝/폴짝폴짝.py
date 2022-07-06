from collections import deque
n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
dp = [10**18]*(n+1)
q = deque([[a, 0]])
dp[a] = 0
while q:
    x, d = q.popleft()

    for i in range(x, n+1, arr[x-1]):
        if dp[i] <= dp[x]+1:
            continue
        dp[i] = dp[x]+1
        q.append([i, dp[x]+1])
    ix = -1
    while True:
        i = x + ix * arr[x-1]
        ix -= 1
        if i <= 0:
            break
        if dp[i] <= dp[x]+1:
            continue
        dp[i] = dp[x] +1
        q.append([i, dp[x]+1])
if dp[b] == 10**18:
    print(-1)
else:
    print(dp[b])