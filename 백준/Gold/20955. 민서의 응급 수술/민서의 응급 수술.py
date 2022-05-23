import sys
input = sys.stdin.readline
n,m=map(int, input().split())
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
ds = DisjointSet(n)
ans = 0
for _ in range(m):
    a,b=map(int, input().split())
    if ds.check(a-1,b-1):
        ans+=1
    else:
        ds.merge(a-1,b-1)
print(ans+len(set([ds.find(i) for i in range(n)]))-1)