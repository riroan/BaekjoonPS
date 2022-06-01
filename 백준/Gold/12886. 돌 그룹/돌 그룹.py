from collections import deque, defaultdict

a, b, c = map(int, input().split())
q = deque()
d = defaultdict(bool)


def f(a, b, c):
    x, y = a, b
    if x > y:
        x, y = y, x
    arr = [x+x, y-x, c]
    arr.sort()
    arr = tuple(arr)
    if not d[arr]:
        q.append(arr)
        d[arr] = True


if a != b:
    f(a, b, c)
if b != c:
    f(b, c, a)
if a != c:
    f(a, c, b)

ok = a==b==c
while q:
    a, b, c = q.popleft()
    if a == b == c:
        ok = True
        break
    if a != b:
        f(a, b, c)
    if b != c:
        f(b, c, a)
    if a != c:
        f(a, c, b)
print(int(ok))