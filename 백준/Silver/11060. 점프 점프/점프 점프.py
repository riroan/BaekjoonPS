from collections import deque
q = deque()
n=int(input())
arr = list(map(int, input().split()))
q.append([0, 0])
dp = [10**18]*n
dp[0] = 0
while q:
    x, d = q.popleft()
    for i in range(1, arr[x]+1):
        if x+i >=n:
            continue
        if dp[x+i] <= dp[x]+1:
            continue
        dp[x+i] = dp[x]+1
        q.append([x+i, dp[x+i]])
if dp[-1] == 10**18:
    print(-1)
else:
    print(dp[-1])