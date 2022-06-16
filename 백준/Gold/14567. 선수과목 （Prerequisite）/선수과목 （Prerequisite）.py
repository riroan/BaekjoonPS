import sys
sys.setrecursionlimit(10**5)


def dfs(x, c=1):
    if dp[x] >= c:
        return
    dp[x] = max(dp[x], c)
    for i in g[x]:
        dfs(i, c+1)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
dp = [0]*(n+1)
g = [[] for i in range(n+1)]
d = [0]*(n+1)
for x, y in arr:
    g[x].append(y)
    d[y] += 1

for i in range(1, n+1):
    if d[i] == 0:
        dfs(i)
print(*dp[1:])