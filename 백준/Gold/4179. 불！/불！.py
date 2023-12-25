# author:  riroan
# created:  2023.12.25 13:16:03
import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
sx, sy = 0, 0
q = deque()
v = [[0]*m for i in range(n)]
brr = [[10**18] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':
            sx, sy = i, j
        if arr[i][j] == 'F':
            q.append((i, j, 0))
            brr[i][j] = 0
            v[i][j] = 1


def check(x, y):
    return 0 <= x < n and 0 <= y < m


while q:
    x, y, d = q.popleft()
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            continue
        if v[tx][ty] or arr[tx][ty] == '#':
            continue
        v[tx][ty] = 1
        brr[tx][ty] = d+1
        q.append((tx, ty, d+1))
v = [[0]*m for i in range(n)]
q = deque()
q.append((sx, sy, 0))
v[sx][sy] = 1
while q:
    x, y, d = q.popleft()
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            print(d+1)
            exit(0)
        if v[tx][ty] or arr[tx][ty] == '#':
            continue
        if brr[tx][ty] <= d+1:
            continue
        v[tx][ty] = 1
        q.append((tx, ty, d+1))
print("IMPOSSIBLE")
