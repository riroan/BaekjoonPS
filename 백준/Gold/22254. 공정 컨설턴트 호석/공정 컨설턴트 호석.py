# author:  riroan
# created:  2024.02.09 12:29:29
import sys
from heapq import *
def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = n+1
while l + 1 < r:
    x = l + r >> 1
    ok = 1
    q = [-k] * x
    for i in arr:
        if not q:
            ok = 0
            break
        t = heappop(q)
        if t + i == 0:
            continue
        elif t + i < 0:
            heappush(q, t+i)
        else:
            check = 0
            while q:
                t = heappop(q)
                if t + i > 0:
                    continue
                if t + i == 0:
                    check = 1
                    break
                if t + i < 0:
                    check = 1
                    heappush(q, t+i)
                    break
            if not check:
                ok = 0
                break
    if ok:
        r = x
    else:
        l = x
print(r)
