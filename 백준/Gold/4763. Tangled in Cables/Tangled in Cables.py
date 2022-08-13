m = float(input())
n=int(input())
d = {}
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
for i in range(n):
    d[input()] = len(d)
edges = []
for i in range(int(input())):
    a,b,c=input().split()
    edges.append((a,b,float(c)))
ds = DisjointSet(n)
edges.sort(key=lambda x:x[2])
ans = 0
for a,b,c, in edges:
    if ds.get(d[a]) == ds.get(d[b]):
        continue
    ds.unite(d[a], d[b])
    ans+=c
if m < ans:
    print("Not enough cable")
else:
    print(f"Need {round(ans,1)} miles of cable")