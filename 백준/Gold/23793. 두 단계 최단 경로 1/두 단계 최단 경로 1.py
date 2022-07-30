n, k = map(int ,input().split())

import heapq

g = [[] for i in range(n)]
arr = [list(map(int, input().split())) for i in range(k)]
for a,b,c in arr:
    a-=1
    b-=1
    g[a].append((b,c))

def dijkstra(start):
    distances = [0] * n
    for i in range(n):
        distances[i] = 987654321000
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in g[current_destination]:
            # new_distance = 1
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances
x,y,z= map(int, input().split())
x-=1
y-=1
z-=1
distances1 = dijkstra(x)
distances2 = dijkstra(y)
ans1 = 0
if distances1[y] >= 98765432100 or distances2[z]>= 98765432100:
    ans1 = -1
else:
    ans1 = distances1[y] + distances2[z]
g = [[]for i in range(n)]
for a,b,c in arr:
    a-=1
    b-=1
    if a == y or b == y:
        continue
    g[a].append((b,c))
distances = dijkstra(x)
if distances[z] >= 98765432100:
    ans = -1
else:
    ans = distances[z]
print(ans1, ans)