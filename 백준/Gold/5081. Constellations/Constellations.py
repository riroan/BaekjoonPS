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
test = 1
while True:
    n=int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for i in range(n)]
    ds = DisjointSet(n)
    for i in range(n):
        m = 10**18
        for j in range(n):
            if i == j:
                continue
            dist = (arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2
            if dist < m:
                m = dist
        for j in range(n):
            if i == j:
                continue
            dist = (arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2
            if dist == m:
                ds.unite(i, j)
    for i in range(n):
        ds.get(i)
    print(f"Sky {test} contains {len(set(ds.p))} constellations.")
    test+=1
