import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
n,m = map(int, input().split())
d= defaultdict(int)
for i in range(n):
    s = input()
    if len(s)<m:
        continue
    d[s]+=1
arr = []
for i in d:
    arr.append((i, d[i]))
arr.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in arr:
    print(i[0])
