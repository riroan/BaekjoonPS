import heapq

n,e = map(int, input().split())

g = [[] for i in range(n)]
for i in range(e):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))

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
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances
a,b=map(int, input().split())
a-=1
b-=1
distances1 = dijkstra(0)
distances2 = dijkstra(a)
distances3 = dijkstra(b)
ans1 = distances1[a] + distances2[b] + distances3[n-1]
ans2 = distances1[b] + distances3[a] + distances2[n-1]
ans = min(ans1, ans2)
if ans >=987654321:
    print(-1)
else:
    print(ans)