from collections import defaultdict

n, m = map(int, input().split())
up = [list(map(int, input().split())) for i in range(n)]
down = [list(map(int, input().split())) for i in range(m)]
u, d = defaultdict(int), defaultdict(int)
for x, y in up:
    u[x] = y
for x, y in down:
    d[x] = y
dp = [99999] * 101


def dfs(x, dist=0):
    global dp
    if x>100:
        return
    if dp[x] <= dist:
        return
    dp[x] = min(dp[x], dist)
    for i in range(1, 7):
        y = x+i
        if u[y]:
            y = u[y]
        if d[y]:
            y = d[y]
        dfs(y, dist+1)

dfs(1)
print(dp[100])