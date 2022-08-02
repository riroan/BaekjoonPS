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
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    ds = DisjointSet(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            x1,y1,x2,y2 = arr[i]
            x3,y3,x4,y4 = arr[j]
            if not (x2<x3 or x4<x1 or y2<y3 or y4<y1):
                ds.unite(i,j)
    for i in range(n):
        ds.get(i)
    print(len(set(ds.p)))