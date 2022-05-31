from collections import deque


def check(x, y, z):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for i in range(n)] for _ in range(h)]
q = deque()
v = [[[False]*m for i in range(n)] for _ in range(h)]
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if arr[k][i][j] == 1:
                v[k][i][j] = True
                q.append((i, j, k, 0))
while q:
    x, y, z, d = q.popleft()
    ans = max(ans, d)
    direct = [[-1, 0, 0], [1, 0, 0], [0, -1, 0],
              [0, 1, 0], [0, 0, 1], [0, 0, -1]]
    for dx, dy, dz in direct:
        tx, ty, tz = x+dx, y+dy, z+dz
        if not check(tx, ty, tz):
            continue
        if v[tz][tx][ty] or arr[tz][tx][ty] == -1:
            continue
        arr[tz][tx][ty] = 1
        v[tz][tx][ty] = 1
        q.append((tx, ty, tz, d+1))
ok = True
for i in range(n):
    for j in range(m):
        for k in range(h):
            if arr[k][i][j] == 0:
                ok = False
if ok:
    print(ans)
else:
    print(-1)
