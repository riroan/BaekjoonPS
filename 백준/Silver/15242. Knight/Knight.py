# author:  riroan
# created:  2024.02.09 12:22:19
from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


n = 8


def check(x, y):
    return 0 <= x < n and 0 <= y < n


a = input()
b = input()
sx, sy = 0, 0
ex, ey = 0, 0
d = {}
for ix, i in enumerate('abcdefgh'):
    d[i] = ix
sx = d[a[0]]
sy = int(a[1]) - 1
ex = d[b[0]]
ey = int(b[1]) - 1

q = deque()
v = [[0]*n for i in range(n)]
q.append((sx, sy, 0))
v[sx][sy] = 1
while q:
    x, y, d = q.popleft()
    if x == ex and y == ey:
        print(d)
        break
    for dx, dy in [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            continue
        if v[tx][ty]:
            continue
        v[tx][ty] = 1
        q.append((tx, ty, d+1))
