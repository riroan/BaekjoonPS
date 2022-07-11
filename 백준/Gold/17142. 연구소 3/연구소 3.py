from itertools import combinations
from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
brr = []
ans = 10**18
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            brr.append((i, j))


def copy(arr, k):
    return [i.copy() for i in arr]


def check(x, y):
    return 0 <= x < n and 0 <= y < n

cc = 0
for i in arr:
    for j in i:
        if j == 0:
            cc+=1

for i in combinations(brr, k):
    a = copy(arr, set(i))
    v = [[0]*n for i in range(n)]
    q = deque()
    tt = cc
    for x, y in i:
        q.append((x, y, 0))
    tmp = -1
    while q:
        x, y, d = q.popleft()
        if d >= ans:
            break
        v[x][y] = d
        tmp = max(tmp, d)
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            tx, ty = x+dx, y+dy
            if not check(tx, ty):
                continue
            if v[tx][ty] or a[tx][ty] == 1:
                continue
            v[tx][ty] = 1
            q.append((tx, ty, d+1))
            if a[tx][ty] == 0:
                tmp = max(tmp, d+1)
                tt-=1
            a[tx][ty] = 3
        if tt == 0:
            break
    if d >= ans:
        continue
    ok = True
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0 and a[i][j] == 0:
                ok = False

    if ok:
        ans = min(ans, tmp)
if ans == 10**18:
    print(-1)
else:
    print(ans)
