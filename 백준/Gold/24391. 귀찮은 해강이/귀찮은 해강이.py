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


n, k = map(int, input().split())
ds = DisjointSet(n)
for i in range(k):
    a, b = map(int, input().split())
    ds.unite(a - 1, b - 1)
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    if ds.get(arr[i-1]-1) != ds.get(arr[i]-1):
        cnt += 1
print(cnt)
