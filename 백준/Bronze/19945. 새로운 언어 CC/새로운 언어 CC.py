# author:  riroan
# created:  2024.02.11 16:25:45
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
if n < 0:
    print(32)
elif n == 0:
    print(1)
else:
    print(len(bin(n))-2)
