import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

d = defaultdict(int)
ans = []
for test in range(int(input())):
    arr = input().split()
    for i in arr[1:]:
        if d[i] == 0:
            d[i] = 1
            ans.append(i)
            break
print(*ans)