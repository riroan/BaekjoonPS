import sys
from collections import deque
sys.setrecursionlimit(10**5)
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y):
    if not check(x, y):
        return
    if v[x][y] or arr[x][y] == 0:
        return
    v[x][y] = True
    brr[x][y] = ix
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        dfs(x+dx, y+dy)


brr = [[0]*n for i in range(n)]

ix = 1
for i in range(n):
    for j in range(n):
        if brr[i][j] == 0 and arr[i][j] != 0:
            v = [[0]*n for i in range(n)]
            dfs(i, j)
            ix += 1

q = deque()
crr = [[None]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if brr[i][j]:
            q.append((brr[i][j], i, j, 0))
while q:
    ix, x, y, d = q.popleft()
    if crr[x][y]:
        continue
    crr[x][y] = (ix, d)
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            continue
        q.append((ix, tx, ty, d+1))
ans = 98765432100
for x in range(n):
    for y in range(n):
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            tx, ty = x+dx, y+dy
            if not check(tx, ty):
                continue
            if crr[x][y] == None or crr[tx][ty] == None:
                continue
            if crr[x][y][0] != crr[tx][ty][0]:
                ans = min(ans, crr[x][y][1]+crr[tx][ty][1])
if ans == 98765432100:
    print(0)
else:
    print(ans)