import sys
def input(): return sys.stdin.readline().strip()


def func(a, b):
    return a+b


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.rangeMin = [0] * (4 * self.n)
        self.init(arr, 0, self.n - 1, 1)

    def init(self, arr, left, right, node):
        if left == right:
            self.rangeMin[node] = arr[left]
            return self.rangeMin[node]
        mid = (left + right) // 2
        leftMin = self.init(arr, left, mid, node * 2)
        rightMin = self.init(arr, mid + 1, right, node * 2 + 1)
        self.rangeMin[node] = func(leftMin, rightMin)
        return self.rangeMin[node]

    def query(self, left, right):
        return self.query2(left, right, 1, 0, self.n - 1)

    def query2(self, left, right, node, nodeLeft, nodeRight):
        if right < nodeLeft or nodeRight < left:
            return 0
        if left <= nodeLeft and nodeRight <= right:
            return self.rangeMin[node]
        mid = (nodeLeft + nodeRight) // 2
        return func(self.query2(left, right, node * 2, nodeLeft, mid),
                    self.query2(left, right, node * 2 + 1, mid + 1, nodeRight))

    def update(self, index, newValue):
        return self.update2(index, newValue, 1, 0, self.n - 1)

    def update2(self, index, newValue, node, nodeLeft, nodeRight):
        if index < nodeLeft or nodeRight < index:
            return self.rangeMin[node]
        if nodeLeft == nodeRight:
            self.rangeMin[node] = newValue
            return self.rangeMin[node]
        mid = (nodeLeft + nodeRight) // 2
        self.rangeMin[node] = func(self.update2(index, newValue, node * 2, nodeLeft, mid),
                                   self.update2(index, newValue, node * 2 + 1, mid + 1, nodeRight))
        return self.rangeMin[node]


def get_score(s):
    score = 0
    f = 1
    flag = 1
    for i in range(len(s)):
        if i and s[i] != s[i-1]:
            flag = 2
        f /= flag
        if s[i] == 'A':
            score += f
        else:
            score -= f
    return score


d = {'A': "B", "B": "A"}

n = int(input())
arr = []
for _ in range(n):
    n, m = map(int, input().split())
    brr = [list(input()) for i in range(n)]
    a = 0
    b = 0
    for i in range(n):
        a += brr[i].count('A')
        b += brr[i].count('B')
    s = 'A'
    if b == 1:
        s = 'B'
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if brr[i][j] == s:
                x, y = i, j
    u, v, w = 0, 0, 0
    pos = []
    ss = set()
    for i in range(n):
        for j in range(m):
            if brr[i][j] != 'C' and brr[i][j] != s:
                if i >= x and j <= y:
                    u += 1
                elif i <= x and j >= y:
                    v += 1
                    pos.append((i, j))
                else:
                    w += 1
                    ss.add((i, j))
    k = w
    for xx, yy in pos:
        cnt = 0
        for i in range(xx, n):
            for j in range(yy+1):
                cnt += (i, j) in ss
        k = min(k, cnt)
    if v == 0:
        s1 = s + d[s] * u
        s2 = d[s] * w
        score = get_score(s1) + get_score(s2)
    else:
        if k == 0:
            score = -1/2**(u+1)+v+w
        else:
            score = -1/2**u+v+w
        if s == 'A':
            score = -score

    arr.append(score)
# print(arr)
st = SegmentTree(arr)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    st.update(a, -st.query(a, a))
    v = st.query(b, c)
    if v > 0:
        print("Ahgus")
    else:
        print("Bagus")