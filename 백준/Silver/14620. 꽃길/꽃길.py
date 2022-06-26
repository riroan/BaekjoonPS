from itertools import combinations
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
p = []
for i in range(1, n-1):
    for j in range(1, n-1):
        p.append((i, j))
ans = 9876543210000


def check(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2) <= 2


for i in combinations(p, 3):
    if check(i[0], i[1]) or check(i[0], i[2]) or check(i[1], i[2]):
        continue
    t = 0
    for x, y in i:
        for dx, dy in [[-1, 0], [0, 1], [0, -1], [1, 0], [0, 0]]:
            tx, ty = x+dx, y+dy
            t+=arr[tx][ty]
    ans = min(ans, t)
print(ans)
