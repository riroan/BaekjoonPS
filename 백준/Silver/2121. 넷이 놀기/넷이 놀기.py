from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort()
d = defaultdict(set)
ans = 0
for x, y in arr:
    d[x].add(y)
for x, y in arr:
    ok = y in d[x+a]
    ok &= (y+b) in d[x]
    ok &= (y+b) in d[x+a]
    if ok:
        ans+=1
print(ans)