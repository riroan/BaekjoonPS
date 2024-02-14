# author:  riroan
# created:  2024.02.14 20:41:46
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [[list(input()) for i in range(5)] for i in range(n)]
ans = 10**18
x,y = 0, 0
for i in range(n):
    for j in range(i+1, n):
        cnt = 0
        for a in range(5):
            for b in range(7):
                cnt += arr[i][a][b] != arr[j][a][b]
        if cnt < ans:
            ans = cnt
            x,y=i,j
print(x+1, y+1)
