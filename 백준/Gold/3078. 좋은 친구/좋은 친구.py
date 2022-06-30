from collections import defaultdict
from bisect import *
n,k = map(int, input().split())
arr = [input() for i in range(n)]
dd =defaultdict(list)
for i in range(n):
    dd[len(arr[i])].append(i)
for i in dd:
    dd[i].append(9999999999)
ans = 0
for i in dd:
    for ix, j in enumerate(dd[i][:-1]):
        l = bisect_left(dd[i], j+k)
        if dd[i][l] - dd[i][ix] <= k:
            ans+=l-ix
        else:
            ans+=l-ix-1
print(ans)