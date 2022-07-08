from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())


def check(x, y):
    return 0 <= x < n and 0 <= y < m


arr = [list(map(int, list(input()))) for i in range(n)]
brr = [arr.copy() for i in range(k+1)]
q = deque([[0, 0, 0, 1]])
v = [[[10**18]*m for i in range(n)] for i in range(k+1)]
v[0][0][0] = 1
ans = 10**18


while q:
    x, y, z, d = q.popleft()
    if x == n-1 and y == m-1:
        ans = min(ans, d)
        continue
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        tx, ty = x+dx, y+dy
        if not check(tx, ty):
            continue
        try:
            if v[z+arr[tx][ty]][tx][ty]<=d+1:
                continue
            v[z+arr[tx][ty]][tx][ty] = d+1
            q.append([tx, ty, z+arr[tx][ty], d+1])
        except:
            continue


if ans == 10**18:
    print(-1)
else:
    print(ans)
