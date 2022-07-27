import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(2*10**5)
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):  # O(logn)
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def merge(self, u, v):  # O(logn)
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            u, v = v, u
        self.parent[u] = v
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1

    def check(self, u, v):
        return self.find(u) == self.find(v)
n,m = map(int, input().split())
g = [[] for i in range(n)]
t = 0
ds = DisjointSet(n)
for i in range(m):
    a,b,c = map(int, input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))
    t+=c
    ds.merge(a,b)

import heapq

pq = []
taken = [0] * (n+1)


def process(vtx):
    global taken, pq
    taken[vtx] = 1
    for i in g[vtx]:
        v, w = i
        if not taken[v]:
            heapq.heappush(pq, (w, i))


process(1)
cost = 0
while pq:
    item = heapq.heappop(pq)
    w = item[0]
    u = item[1][0]
    if not taken[u]:
        cost += w
        process(u)
tmp = [ds.find(i) for i in range(n)]
if len(set(tmp))>1:
    print(-1)
else:
    print(t-cost)