import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

for test in range(int(input())):
    n=int(input())
    high = []
    low = []
    d = defaultdict(int)
    for i in range(n):
        a,b = input().strip().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(high, -b)
            heapq.heappush(low, b)
            d[b] +=1
        else:
            try:
                if b == 1:
                    t = -heapq.heappop(high)
                    while d[t] == 0:
                        t = -heapq.heappop(high)
                    d[t]-=1
                else:
                    t = heapq.heappop(low)
                    while d[t] == 0:
                        t = heapq.heappop(low)
                    d[t]-=1
            except:
                pass
    ok = True
    m = 10**10
    mm = -10**10
    for i in d:
        if d[i]:
            m = min(m, i)
            mm = max(mm, i)
            ok = False
    if ok:
        print("EMPTY")
    else:
        print(mm, m)