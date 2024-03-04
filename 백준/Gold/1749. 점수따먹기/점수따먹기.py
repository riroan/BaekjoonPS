# author:  riroan
# created:  2024.03.05 02:30:19
import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]


def get(a, b, c, d):
    if a == 0 and b == 0:
        return s[c][d]
    elif a == 0:
        return s[c][d] - s[c][b - 1]
    elif b == 0:
        return s[c][d] - s[a - 1][d]
    else:
        return s[c][d] - s[c][b - 1] - s[a - 1][d] + s[a - 1][b - 1]


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
ma = -10**18
for dx in range(n+1):
    for dy in range(m+1):
        for x in range(n-dx):
            for y in range(m-dy):
                ma = max(ma, get(x, y, x+dx, y+dy))
print(ma)
