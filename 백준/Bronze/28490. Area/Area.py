# author:  riroan
# created:  2023.11.22 13:58:40
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 0
for x,y in arr:
    ans = max(ans, x*y)
print(ans)
