from collections import deque

def check(x,y):
    return 0<=x<n and 0<=y<m

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
q = deque()
v = [[False]*m for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            v[i][j] = True
            q.append((i,j,0))
while q:
    x,y,d = q.popleft()
    ans = max(ans, d)
    direct = [[-1,0],[1,0],[0,-1],[0,1]]
    for dx, dy in direct:
        tx,ty = x+dx, y+dy
        if not check(tx,ty):
            continue
        if v[tx][ty] or arr[tx][ty] == -1:
            continue
        arr[tx][ty] = 1
        v[tx][ty] = 1
        q.append((tx,ty, d+1))
ok = True
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ok = False
if ok:
    print(ans)
else:
    print(-1)