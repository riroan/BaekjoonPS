from collections import defaultdict
import sys
input = sys.stdin.readline
import string
s = input().strip()
d = defaultdict(list)
for i in s:
    for j in string.ascii_lowercase:
        d[j].append(int(i==j))
ps = defaultdict(list)
for i in d:
    p = [0]
    for j in d[i]:
        p.append(p[-1]+j)
    ps[i] = p
for i in range(int(input())):
    a, b, c = input().strip().split()
    b = int(b)
    c = int(c)
    print(ps[a][c+1]-ps[a][b])