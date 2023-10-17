# author:  riroan
# created:  2023.10.17 21:45:47
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    a,b=map(int, input().split())
    print(["NO BRAINS", "MMM BRAINS"][a>=b])
