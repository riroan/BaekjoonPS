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
n,m,q = map(int, input().split())
ds = DisjointSet(n)
for i in range(m):
    a,b = map(int, input().split())
    ds.unite(a-1,b-1)
for i in range(q):
    a,b=map(int, input().split())
    if ds.get(a-1) == ds.get(b-1):
        print("Y")
    else:
        print("N")