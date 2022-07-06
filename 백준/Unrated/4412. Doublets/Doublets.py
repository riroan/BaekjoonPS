from collections import deque
import string
import heapq
arr = []
g = {}
d = {}
dd = {}
while True:
    s = input()
    if len(s) == 0:
        break
    arr.append(s)
    d[s] = len(d)
    dd[len(dd)] = s
    if s not in g:
        g[s] = []
    for i in range(len(s)):
        
        for j in string.ascii_lowercase:
            tmp = list(s)
            if s[i] == j:
                continue
            tmp[i] = j
            tmp = ''.join(tmp)
            if tmp in g:
                g[s].append(tmp)
                g[tmp].append(s)

def dijkstra(start, end):
    parents = {}
    distances = {}
    for c in arr:
        distances[c] = 10**18
        if c != start:
            parents[c] = ''
    distances[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        curr_cost, curr = heapq.heappop(pq)
        if distances[curr]<curr_cost:
            continue
        for next in g[curr]:
            next_cost = 1
            if curr_cost + next_cost < distances[next]:
                heapq.heappush(pq, (curr_cost + 1, next))
                distances[next] = curr_cost + 1
                parents[next] = curr
    route = []
    current = end
    ok = True
    while current != start:
        route.append(current)
        current = parents[current]
        if current == '':
            ok = False
            break
    route.append(start)
    route.reverse()
    if ok:
        for i in route:
            print(i)
    else:
        print("No solution.")

try:
    ok = False
    while True:
        a, b = input().split()
        if ok:
            print()
        dijkstra(a,b)
        ok = True
except:
    pass