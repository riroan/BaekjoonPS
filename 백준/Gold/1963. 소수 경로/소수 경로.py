import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def check(a, b):
    a = str(a)
    b = str(b)
    cnt = 0
    for i, j in zip(a, b):
        cnt += i != j
    return cnt == 1


p = []
for i in range(1000, 10000):
    if isPrime(i):
        p.append(i)
d = {}
for i in range(len(p)):
    d[p[i]] = i
g = [[] for i in range(len(p))]
for i in range(len(p)):
    for j in range(len(p)):
        if check(p[i], p[j]):
            g[i].append(j)
            g[j].append(i)

for test in range(int(input())):
    a, b = map(int, input().split())
    a = d[a]
    b = d[b]
    q = deque()
    q.append((a, 0))
    v = [0]*len(p)
    v[a] = 1
    while q:
        x, dist = q.popleft()
        if x == b:
            break
        for i in g[x]:
            if not v[i]:
                q.append((i, dist+1))
                v[i] = 1
    print(dist)
