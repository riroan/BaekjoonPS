import sys
input = lambda: sys.stdin.readline().strip()
class DisjointSet:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.size = [1]*n

    def get(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.get(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x,y=y,x
            self.p[y] = x
            self.size[x] += self.size[y]
            self.size[y] = 0
            return True
        return False
for test in range(int(input())):
    n=int(input())
    arr = [input().split() for i in range(n)]
    d = {}
    for x,y in arr:
        if x not in d:
            d[x] = len(d)
        if y not in d:
            d[y] = len(d)
    ds = DisjointSet(len(d))
    for x,y in arr:
        ds.unite(d[x],d[y])
        print(max(ds.size[ds.get(d[x])], ds.size[ds.get(d[y])]))