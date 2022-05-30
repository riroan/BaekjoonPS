import sys

input = sys.stdin.readline

MAX = 1 << 21


def func(a, b):
    return a + b


class ST:
    def __init__(self):
        self.start = MAX // 2
        self.arr = [0] * MAX
        self.lazy = [0] * MAX

    def build(self):
        for i in range(self.start - 1, 0, -1):
            self.arr[i] = func(self.arr[i * 2], self.arr[i * 2 + 1])

    def propagate(self, node, l, r):
        if self.lazy[node] != 0:
            if node < self.start:
                self.lazy[node * 2] = func(self.lazy[node * 2], self.lazy[node])
                self.lazy[node * 2 + 1] = func(self.lazy[node * 2 + 1], self.lazy[node])
            self.arr[node] += self.lazy[node] * (r-l)
            self.lazy[node] = 0

    def update(self, s, e, k):
        self.update2(s, e, k, 1, 0, self.start)

    def update2(self, s, e, k, node, l, r):
        self.propagate(node, l, r)
        if e <= l or r <= s:
            return
        if s <= l and r <= e:
            self.lazy[node] = func(self.lazy[node], k)
            self.propagate(node, l, r)
            return
        mid = (l + r) // 2
        self.update2(s, e, k, node * 2, l, mid)
        self.update2(s, e, k, node * 2 + 1, mid, r)
        self.arr[node] = func(self.arr[node * 2], self.arr[node * 2 + 1])

    def query(self, s, e):
        return self.query2(s, e, 1, 0, self.start)

    def query2(self, s, e, node, l, r):
        self.propagate(node, l, r)
        if e <= l or r <= s:
            return 0
        if s <= l and r <= e:
            return self.arr[node]
        mid = (l + r) // 2
        return func(self.query2(s, e, node * 2, l, mid), self.query2(s, e, node * 2 + 1, mid, r))


n, m, k = map(int, input().split())

tree = ST()
for i in range(n):
    tree.arr[tree.start + i] = int(input())
tree.build()

for _ in range(k + m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a, b, c = op[1], op[2], op[3]
        tree.update(a - 1, b, c)
    else:
        a, b = op[1], op[2]
        print(tree.query(a - 1, b))