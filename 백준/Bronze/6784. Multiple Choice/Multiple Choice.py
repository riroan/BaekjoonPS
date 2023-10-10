# author:  riroan
# created:  2023.10.10 10:03:40
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [input() for i in range(n)]
brr = [input() for i in range(n)]
ans = 0
for i,j in zip(arr, brr):
    ans +=i==j
print(ans)
