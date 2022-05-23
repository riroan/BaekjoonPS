import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
arr = [list(input()) for i in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def check(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    global v
    if not check(x, y):
        return
    if v[x][y]:
        return
    v[x][y] = True
    if arr[x][y] in '1#':
        brr[x][y] = '0'
        return
    for dx, dy in d:
        dfs(x+dx, y+dy)


ans = 0
while arr[x2][y2] == '#':
    v = [[False] * m for i in range(n)]
    brr = [i.copy() for i in arr]
    dfs(x1, y1)
    arr = brr
    ans+=1
print(ans)