# author:  riroan
# created:  2023.12.17 17:55:08
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
brr = []
for i in range(n):
    for j in range(n):
        brr.append((arr[i][j], i, j))
brr.sort()
dp = [[0]*n for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < n


for t, x, y in brr:
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        tx, ty = x+dx, y+dy
        if not check(tx,ty):
            continue
        if arr[tx][ty] >= t:
            continue
        dp[x][y] = max(dp[x][y], dp[tx][ty] + 1)
ans = 0
for i in dp:
    ans = max(ans, max(i))
print(ans+1)
