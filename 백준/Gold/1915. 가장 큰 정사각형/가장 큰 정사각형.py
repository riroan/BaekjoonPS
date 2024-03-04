# author:  riroan
# created:  2024.03.05 02:11:25
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
arr = [list(map(int, list(input()))) for i in range(n)]
s = [[0] * m for _ in range(n)]
s[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        # 꼭대기
        if i == 0:
            if j == 0:
                continue
            s[0][j] = s[0][j - 1] + arr[0][j]
        # 왼쪽
        elif j == 0:
            s[i][j] = s[i - 1][j] + arr[i][j]
        else:
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + arr[i][j]
l = 0
r = min(n, m)+1
while l + 1 < r:
    x = l + r >> 1
    ok = 0
    for i in range(n-x+1):
        for j in range(m-x+1):
            if get(i, j, i+x-1, j+x-1) == x**2:
                ok = 1
                break
        else:
            continue
        break
    if ok:
        l = x
    else:
        r = x
print(l**2)
