# author:  riroan
# created:  2023.10.16 21:14:24
import sys
input = lambda: sys.stdin.readline().strip()

c,k,p = map(int, input().split())
ans = 0
for i in range(1, c+1):
    ans += k*i+p*i**2
print(ans)
