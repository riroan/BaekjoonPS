# author:  riroan
# created:  2024.03.10 22:15:08
import sys
input = lambda: sys.stdin.readline().strip()

n, m= map(int, input().split())
arr = [list(input()) for i in range(n)]
row = []
col = []
for i in range(n):
    cnt = arr[i].count('X')
    row.append(cnt)
for j in range(m):
    cnt = 0
    for i in range(n):
        cnt += arr[i][j] == 'X'
    col.append(cnt)
print(max(row.count(0), col.count(0)))
