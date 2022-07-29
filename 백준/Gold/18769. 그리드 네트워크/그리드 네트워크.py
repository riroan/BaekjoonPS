import sys
input = lambda: sys.stdin.readline().strip()

def get(x,y):
    return x*c+y
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

for test in range(int(input())):
    r,c = map(int, input().split())
    arr=  [list(map(int, input().split())) for i in range(r)]
    brr=  [list(map(int, input().split())) for i in range(r-1)]
    edges = []
    for i in range(r):
        for j in range(c-1):
            a = get(i, j)
            b = get(i, j+1)
            edges.append((a,b,arr[i][j]))
    for i in range(r-1):
        for j in range(c):
            a = get(i,j)
            b = get(i+1, j)
            edges.append((a,b,brr[i][j]))
    ds = DisjointSet(r*c)
    edges.sort(key=lambda x: x[2])
    ans = 0
    for x,y,d in edges:
        if ds.get(x) != ds.get(y):
            ans+=d
            ds.unite(x,y)
    print(ans)