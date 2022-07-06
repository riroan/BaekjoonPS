from collections import deque
n, m, r = map(int, input().split())
g = [[] for i in range(n+1)]
v = [-1] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
q = deque([(r, 0)])
v[r] = 0
while q:
    x, d = q.popleft()
    for i in g[x]:
        if v[i] != -1:
            continue
        q.append((i, d+1))
        v[i] = d+1
for i in v[1:]:
    print(i)