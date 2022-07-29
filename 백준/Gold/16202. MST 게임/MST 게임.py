class DisjointSet:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def get(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.get(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x != y:
            self.p[x] = y
            return True
        return False

n,m, k = map(int, input().split())
edges = [list(map(int, input().split())) + [i+1] for i in range(m)]
edges = [[x-1,y-1,z] for x,y,z in edges]
ans = [0]*k
for j in range(k):
    edges.sort(key = lambda x:x[2])
    ds = DisjointSet(n)
    m = 987654321
    ret = 0
    for x,y,z in edges:
        if ds.get(x) != ds.get(y):
            m = min(m, z)
            ds.unite(x,y)
            ret += z
    p = set()
    for i in range(n):
        p.add(ds.get(i))
    if len(p) >= 2:
        break
    edges = [edge for edge in edges if edge[2] != m]
    ans[j] = ret
print(*ans)