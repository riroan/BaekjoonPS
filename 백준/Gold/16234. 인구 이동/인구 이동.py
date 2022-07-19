n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

def check(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y):
    global path
    path.append((x,y))
    for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
        tx,ty = x+dx,y+dy
        if not check(tx,ty):
            continue
        if v[tx][ty]:
            continue
        # if (tx,ty) not in s:
        #     continue
        if l<=abs(arr[x][y] - arr[tx][ty])<=r:
            v[tx][ty] = 1
            dfs(tx,ty)


ans = 0
while True:
    s = set()
    # for i in range(n):
    #     for j in range(n):
    #         if l <= arr[i][j] <= r:
    #             s.add((i, j))
    v = [[0] * n for i in range(n)]
    ok = False
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                v[i][j] = 1
                path = []
                dfs(i,j)
                ss = 0
                for x,y in path:
                    ss+=arr[x][y]
                diff = 0
                ss//=len(path)
                for x,y in path:
                    diff += abs(arr[x][y] - ss)
                    arr[x][y] = ss
                if diff:
                    ok = True
    if not ok:
        break
    ans+=1
    # for i in arr:
    #     print(*i)
    # print()
print(ans)
