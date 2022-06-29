import heapq

n, m = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
pq = []
taken = [0] * (n+1)


def process(vtx):
    global taken, pq
    taken[vtx] = 1
    for i in g[vtx]:
        v, w = i
        if not taken[v]:
            heapq.heappush(pq, (w, i))


process(1)
cost = 0
while pq:
    item = heapq.heappop(pq)
    w = item[0]
    u = item[1][0]
    if not taken[u]:
        cost += w
        process(u)
print(cost)
