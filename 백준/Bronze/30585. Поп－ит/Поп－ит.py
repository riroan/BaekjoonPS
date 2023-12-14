# author:  riroan
# created:  2023.12.14 14:14:37
import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int, input().split())
a,b = 0, 0
for i in range(n):
    s = input()
    a += s.count('1')
    b += s.count('0')
print(min(a,b))
