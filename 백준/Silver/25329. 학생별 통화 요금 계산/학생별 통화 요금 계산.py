from collections import defaultdict
from math import ceil
n = int(input())
dd = defaultdict(int)
for i in range(n):
    a, b = input().split()
    h, m = map(int, a.split(":"))
    t = h*60+m
    dd[b] += t
cost = defaultdict(int)
for i in dd:
    cost[i] = 10
    dd[i]-=100
    if dd[i]>0:
        cost[i] += ceil(dd[i]/50)*3
arr = [[cost[i], i]for i in cost]
arr.sort(key=lambda x:(-x[0],x[1]))
for x,y in arr:
    print(y,x)
