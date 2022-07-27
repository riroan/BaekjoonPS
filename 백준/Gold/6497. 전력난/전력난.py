import heapq
import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(3*10**5)



def process(vtx):
    global taken, pq
    taken[vtx] = 1
    for i in g[vtx]:
        v, w = i
        if not taken[v]:
            heapq.heappush(pq, (w, i))




while True:
    n,b = map(int, input().split())
    if n+b==0:
        break
    g = [[] for i in range(n)]
    t = 0
    for i in range(b):
        x,y,z = map(int, input().split())
        g[x].append((y,z))
        g[y].append((x,z))
        t+=z
    
    pq = []
    taken = [0] * (n+1)
    process(1)
    cost = 0
    while pq:
        item = heapq.heappop(pq)
        w = item[0]
        u = item[1][0]
        if not taken[u]:
            cost += w
            process(u)
    print(t-cost)
