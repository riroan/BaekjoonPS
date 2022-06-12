import sys
sys.setrecursionlimit(10**5)
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

cnt = [[0]*m for i in range(n)]
d = [[[-1, -1]for i in range(m)] for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    ix, iy = -1, -1
    m = arr[x][y]
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            continue
        if arr[tx][ty] < m:
            m = arr[tx][ty]
            ix, iy = tx, ty
    if m == arr[x][y]:
        d[x][y] = [x, y]
        return [x, y]
    else:
        if d[ix][iy] != [-1,-1]:
            d[x][y] = d[ix][iy]
            return d[x][y]
        p = dfs(ix, iy)
        d[x][y] = p
        return p


for i in range(n):
    for j in range(m):
        if d[i][j] == [-1, -1]:
            dfs(i, j)
for i in range(n):
    for j in range(m):
        x, y = d[i][j]
        cnt[x][y] += 1

for i in cnt:
    print(*i)
