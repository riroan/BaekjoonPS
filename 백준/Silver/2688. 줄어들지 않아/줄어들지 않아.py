from math import *
import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n = int(input())
    ans = 1
    for i in range(9):
        ans *= (n+9-i)
        ans//=(i+1)
    print(ans)