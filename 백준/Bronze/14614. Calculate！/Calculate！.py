# author:  riroan
# created:  2023.10.24 19:15:40
import sys
input = lambda: sys.stdin.readline().strip()

a,b,c = map(int, input().split())
if c&1:
    print(a^b)
else:
    print(a)
