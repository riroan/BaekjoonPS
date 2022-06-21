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

def func2(a,b):
    return min(a,b)
class RMQ:
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
        self.arr[node] = func2(l, r)
        return self.arr[node]

    def propagate(self, node, nodeLeft, nodeRight):
        if self.lazy[node] != 0:
            if nodeLeft != nodeRight:
                self.lazy[node *
                          2] = func(self.lazy[node * 2], self.lazy[node])
                self.lazy[node * 2 +
                          1] = func(self.lazy[node * 2 + 1], self.lazy[node])
            self.arr[node] = func(
                self.arr[node], self.lazy[node])
            self.lazy[node] = 0

    def query(self, left, right):
        return self.query2(left, right, 1, 0, self.n - 1)

    def query2(self, left, right, node, nodeLeft, nodeRight):
        self.propagate(node, nodeLeft, nodeRight)
        if right < nodeLeft or nodeRight < left:
            return 999999998999999
        if left <= nodeLeft and nodeRight <= right:
            return self.arr[node]
        mid = (nodeLeft + nodeRight) // 2
        return func2(self.query2(left, right, node * 2, nodeLeft, mid),
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
        self.arr[node] = func2(self.update2(left, right, newValue, node * 2, nodeLeft, mid),
                              self.update2(left, right, newValue, node * 2 + 1, mid + 1, nodeRight))
        return self.arr[node]


n,q=map(int, input().split())
arr = list(map(int, input().split()))
lst = Tree(arr)
rmq = RMQ(arr)
for i in range(q):
    op = input().split()
    if op[0] == 'M':
        a,b= list(map(int, op[1:]))
        print(rmq.query(a-1, b-1))
    elif op[0] == 'S':
        a,b= list(map(int, op[1:]))
        print(lst.query(a-1,b-1))
    else:
        a,b,c= list(map(int, op[1:]))
        lst.update(a-1,b-1,c)
        rmq.update(a-1,b-1,c)