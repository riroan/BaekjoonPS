from collections import defaultdict
import sys
input = sys.stdin.readline
s = defaultdict(str)
for j in [input().strip() for i in range(int(input()))]:
    u =list(j)
    u.sort()
    if s[tuple(u)]:
        continue
    s[tuple(u)] = j
for i in s:
    print(s[i])