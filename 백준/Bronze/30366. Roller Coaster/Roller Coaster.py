# author:  riroan
# created:  2023.10.20 20:52:49
import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int, input().split())
arr = list(map(int, input().split()))
x = 0
cur = 0
for i in arr:
    if x + i > m:
        cur+=1
        x = 0
    x+=i
    print(cur)
