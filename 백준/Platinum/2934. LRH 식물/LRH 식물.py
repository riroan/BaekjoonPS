import sys
def input(): return sys.stdin.readline().strip()


def func(a, b):
    return a + b


class Tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.init(arr, 0, self.n - 1, 1)

    def init(self, arr, left, right, node):
        if left == right:
            self.arr[node] = arr[left]
            return self.arr[node]
        mid = (left + right) // 2
        l = self.init(arr, left, mid, node * 2)
        r = self.init(arr, mid + 1, right, node * 2 + 1)
        self.arr[node] = func(l, r)
        return self.arr[node]

    def propagate(self, node, nodeLeft, nodeRight):
        if self.lazy[node] != 0:
            if nodeLeft != nodeRight:
                self.lazy[node *
                          2] = func(self.lazy[node * 2], self.lazy[node])
                self.lazy[node * 2 +
                          1] = func(self.lazy[node * 2 + 1], self.lazy[node])
            self.arr[node] = func(
                self.arr[node], self.lazy[node] * (nodeRight - nodeLeft + 1))
            self.lazy[node] = 0

    def query(self, left, right):
        return self.query2(left, right, 1, 0, self.n - 1)

    def query2(self, left, right, node, nodeLeft, nodeRight):
        self.propagate(node, nodeLeft, nodeRight)
        if right < nodeLeft or nodeRight < left:
            return 0
        if left <= nodeLeft and nodeRight <= right:
            return self.arr[node]
        mid = (nodeLeft + nodeRight) // 2
        return func(self.query2(left, right, node * 2, nodeLeft, mid),
                    self.query2(left, right, node * 2 + 1, mid + 1, nodeRight))

    def update(self, left, right, newValue):
        return self.update2(left, right, newValue, 1, 0, self.n - 1)

    def update2(self, left, right, newValue, node, nodeLeft, nodeRight):
        self.propagate(node, nodeLeft, nodeRight)
        if right < nodeLeft or nodeRight < left:
            return self.arr[node]
        if left <= nodeLeft and nodeRight <= right:
            self.lazy[node] = func(self.lazy[node], newValue)
            self.propagate(node, nodeLeft, nodeRight)
            return self.arr[node]
        mid = (nodeLeft + nodeRight) // 2
        self.arr[node] = func(self.update2(left, right, newValue, node * 2, nodeLeft, mid),
                              self.update2(left, right, newValue, node * 2 + 1, mid + 1, nodeRight))
        return self.arr[node]


arr = [0]*100000
tree = Tree(arr)
ans = [0]*100000
lst = Tree(arr)
for i in range(int(input())):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l+1 <= r-1:
        tree.update(l+1, r-1, 1)
    # for i in range(10):
    #     print(tree.query(i, i), end=" ")
    # print()
    # for i in range(10):
    #     print(tree.query(i, i), end=" ")
    # print()
    x = tree.query(l, l)
    y = tree.query(r, r)
    print(x+y)
    tree.update(l, l, -x)
    tree.update(r, r, -y)
