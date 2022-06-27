import heapq

n, d = map(int, input().split())
g = [[] for i in range(10001)]
for i in range(n):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
for i in range(10000):
    g[i].append((i+1, 1))


def dijkstra(start):
    distances = [0] * 10001
    for i in range(10001):
        distances[i] = 987654321000
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if distances[current_destination] < current_distance:
            continue
        for new_destination in g[current_destination]:
            new_distance = new_destination[1]
            distance = current_distance + new_distance
            if distance < distances[new_destination[0]]:
                distances[new_destination[0]] = distance
                heapq.heappush(q, [distance, new_destination[0]])
    return distances

distances = dijkstra(0)
print(distances[d])