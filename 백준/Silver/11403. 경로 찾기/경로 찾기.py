n = int(input())
g = [list(map(int, input().split())) for i in range(n)]
ans = [[0]*n for i in range(n)]


def dfs(x):
    global v, ans
    if v[x]:
        return
    v[x] = True
    for i in range(n):
        if g[x][i]:
            ans[start][i] = 1
            dfs(i)
            


for start in range(n):
    v = [0]*n
    dfs(start)
for i in ans:
    print(*i)