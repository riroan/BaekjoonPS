import heapq
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
g = [[]for i in range(n)]
for i in range(int(input())):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
ans = 0

def dijkstra(start):
    global ans
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

def dijkstra2(start):
    global ans
    distances = [0] * n
    for i in range(n):
        distances[i] = 987654321000
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start, arr[start]])
    while q:
        current_distance, current_destination, value = heapq.heappop(q)
        
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in g[current_destination]:
            distance = current_distance + new_distance
            if t == new_destination and distance == dist:
                ans = max(ans, value + arr[new_destination])
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination, value + arr[new_destination]])
    return distances

s, t = map(int, input().split())
s -= 1
t -= 1
distance = dijkstra(s)
dist = distance[t]
if dist == 987654321000:
    print(-1)
else:
    dijkstra2(s)
    print(dist, ans)