import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def check(x, y):
    return 0 <= x < n and 0 <= y < n


for test in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    v = [[0]*n for i in range(n)]
    q = deque()
    q.append((sx,sy,0))
    v[sx][sy] = 1
    while q:
        x,y,cnt = q.popleft()
        if x == ex and y == ey:
            print(cnt)
            break
        for dx, dy in [[-2,1],[-2,-1],[2,-1],[2,1],[1,2],[1,-2],[-1,-2],[-1,2]]:
            if check(x+dx,y+dy):
                if v[x+dx][y+dy] == 0:
                    v[x+dx][y+dy] = 1
                    q.append((x+dx,y+dy, cnt+1))