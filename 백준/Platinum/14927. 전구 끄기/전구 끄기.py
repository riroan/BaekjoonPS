n = int(input())
ans = 9876543210
arr = [list(map(int, input().split())) for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(2**n):
    brr = [i.copy() for i in arr]
    cnt = 0
    for j in range(n):
        if (1 << j) & i:
            x, y = 0, j
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0,-1], [0, 0]]:
                tx, ty = x+dx, y+dy
                if not check(tx, ty):
                    continue
                brr[tx][ty] ^= 1
            cnt += 1
    for x in range(1, n):
        for y in range(n):
            if brr[x-1][y]:
                for dx, dy in [[-1, 0], [0, 1], [1, 0], [0,-1], [0, 0]]:
                    tx, ty = x+dx, y+dy
                    if not check(tx, ty):
                        continue
                    brr[tx][ty] ^= 1
                cnt+=1
    ok = True
    for i in range(n):
        for j in range(n):
            if brr[i][j]:
                ok = False
    if ok:
        ans = min(ans, cnt)
if ans<9876543210:
    print(ans)
else:
    print(-1)