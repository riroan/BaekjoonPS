import heapq

n,m,k,x=map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    g[a-1].append(b-1)

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
        for new_destination in g[current_destination]:
            new_distance = 1
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances
arr = dijkstra(x-1)
ok = False
for i in range(len(arr)):
    if arr[i] == k:
        ok = True
        print(i+1)
if not ok:
    print(-1)
