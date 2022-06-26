import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n = int(input())
    arr = [(input(), input()) for i in range(n)]
    d = defaultdict(int)
    g = {}
    for i, j in arr:
        d[i] += 1
        d[j] += 1
        g[i] = j
    s = []
    for i in d:
        if d[i] == 1:
            s.append(i)
    if s[0] in g:
        a = s[0]
    else:
        a = s[1]
    print(f"Case #{test+1}:",end=" ")
    while a in g:
        print(f'{a}-{g[a]}',end=" ")
        a = g[a]
    print()
