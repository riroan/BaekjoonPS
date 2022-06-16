from collections import deque


def check(x, y, z):
    return 0 <= x < a and 0 <= y < b and 0 <= z < c


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    arr = []
    for i in range(a):
        brr = [list(input()) for i in range(b)]
        arr.append(brr)
        input()
    v = [[[False]*c for i in range(b)] for j in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    x, y, z = i, j, k
                if arr[i][j][k] == 'E':
                    ex, ey, ez = i, j, k
    q = deque()
    q.append([x, y, z, 0])
    v[x][y][z] = True
    ok = False
    while q:
        x, y, z, d = q.popleft()
        if x == ex and y == ey and z == ez:
            print(f"Escaped in {d} minute(s).")
            ok = True
            break
        for dx, dy, dz in [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, -1], [0, 0, 1]]:
            tx, ty, tz = x+dx, y+dy, z+dz
            if not check(tx,ty,tz):
                continue
            if v[tx][ty][tz] or arr[tx][ty][tz] == '#':
                continue
            v[tx][ty][tz] = True
            q.append([tx,ty,tz,d+1])
    if not ok:
        print("Trapped!")