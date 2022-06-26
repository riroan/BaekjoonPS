from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < m


ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            v = [[0] * m for i in range(n)]
            d = 0
            q = deque()
            v[i][j] = 1
            q.append((i, j, d))
            while q:
                x, y, d = q.popleft()
                ans = max(ans, d)
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    tx, ty = x+dx, y+dy
                    if not check(tx, ty):
                        continue
                    if v[tx][ty] or arr[tx][ty] == 'W':
                        continue
                    v[tx][ty] = 1
                    q.append((tx, ty, d+1))
print(ans)
