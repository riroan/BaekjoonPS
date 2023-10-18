# author:  riroan
# created:  2023.10.19 08:48:47
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n = int(input())
    print([0, n*(n//2-1)][n%2==0])
