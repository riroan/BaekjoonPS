import sys
from bisect import *
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    brr.sort()
    ans = 0
    for i in arr:
        ix = bisect_left(brr, i)
        tmp = 10**18
        x = 0
        for j in range(-1, 2):
            t = ix+j
            if 0<=t<m:
                if tmp > abs(i - brr[t]):
                    tmp = abs(i - brr[t])
                    x = brr[t]
        ans+=x
    print(ans)