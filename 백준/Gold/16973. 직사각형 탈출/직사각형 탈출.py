# author:  riroan
# created:  2024.03.09 23:14:48
import heapq
import sys
def input(): return sys.stdin.readline().strip()


def get(a, b, c, d):
    if a == 0 and b == 0:
        return s[c][d]
    elif a == 0:
        return s[c][d] - s[c][b - 1]
    elif b == 0:
        return s[c][d] - s[a - 1][d]
    else:
        return s[c][d] - s[c][b - 1] - s[a - 1][d] + s[a - 1][b - 1]


n, m = map(int, input().split())


def check(x, y):
    return 0 <= x < n and 0 <= y < m


arr = [list(map(int, input().split())) for i in range(n)]
w, h, sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

s = [[0] * m for _ in range(n)]
s[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                continue
            s[0][j] = s[0][j - 1] + arr[0][j]
        elif j == 0:
            s[i][j] = s[i - 1][j] + arr[i][j]
        else:
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + arr[i][j]
g = [[] for i in range(n*m)]
for x in range(n-w+1):
    for y in range(m-h+1):
        if get(x, y, x+w-1, y+h-1) > 0:
            continue
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            tx, ty = x+dx, y+dy
            if not check(tx, ty):
                continue
            if not check(tx+w-1, ty+h-1):
                continue
            ss = get(tx, ty, tx+w-1, ty+h-1)
            if ss > 0:
                continue
            g[x*m+y].append(tx*m+ty)


def dijkstra(start):
    distances = [0] * (n*m)
    for i in range(n*m):
        distances[i] = 987654321000
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if distances[current_destination] < current_distance:
            continue
        for new_destination in g[current_destination]:
            new_distance = 1
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances


g = dijkstra(sx*m+sy)
ans = g[ex*m+ey]
if ans == 987654321000:
    print(-1)
else:
    print(ans)
