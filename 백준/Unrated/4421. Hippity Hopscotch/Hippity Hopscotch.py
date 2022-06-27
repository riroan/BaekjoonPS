n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[-1]*n for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, d=0):
    if not check(x, y):
        return
    if dp[x][y] >= d:
        return
    dp[x][y] = d
    for i in range(x-k, x+k+1):
        if check(i, y):
            if arr[i][y] > arr[x][y]:
                dfs(i, y, d + arr[i][y])
    for i in range(y-k, y+k+1):
        if check(x, i):
            if arr[x][i] > arr[x][y]:
                dfs(x, i, d + arr[x][i])
dfs(0,0, arr[0][0])
ans = 0
for i in dp:
    ans = max(ans, max(i))
print(ans)