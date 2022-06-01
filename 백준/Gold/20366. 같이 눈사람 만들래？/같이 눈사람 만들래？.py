from collections import defaultdict
from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
d = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        d[arr[i]+arr[j]].append((i, j))
m = 987654321000000


def check(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1 == x2 or x1 == y2 or y1 == x2 or y1 == y2

k = list(d.keys())
k.sort()
for i in range(len(k)):
    j = bisect_left(k, k[i])
    for u in range(j, len(k)):
        flag = False
        if abs(k[i]-k[u]) < m:
            for x in d[k[i]]:
                for y in d[k[u]]:
                    ok = False
                    if not check(x,y):
                        ok = True
                        m = abs(k[i]-k[u])
                        flag = True
                        break
        else:
            break
    for u in range(j, i-1,-1):
        flag = False
        if abs(k[i]-k[u]) < m:
            for x in d[k[i]]:
                for y in d[k[u]]:
                    ok = False
                    if not check(x, y):
                        ok = True
                        m = abs(k[i]-k[u])
                        flag = True
                        break
        else:
            break
print(m)