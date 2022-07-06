from collections import deque
n, m, r = map(int, input().split())
g = [[] for i in range(n+1)]
v = [-1] * (n+1)
t = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
q = deque([(r, 0)])
ix = 1
v[r] = 0
t[r] = ix
ix+=1
while q:
    x, d = q.popleft()
    for i in g[x]:
        if v[i] != -1:
            continue
        q.append((i, d+1))
        v[i] = d+1
        t[i] = ix
        ix+=1
ans = 0
for i,j in zip(v[1:], t[1:]):
    ans+=i*j
print(ans)