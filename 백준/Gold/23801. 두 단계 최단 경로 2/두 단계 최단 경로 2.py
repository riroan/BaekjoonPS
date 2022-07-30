import heapq
import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))

def dijkstra(start):
    distances = [0] * n
    for i in range(n):
        distances[i] = 987654321123456789
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
start, end = map(int, input().split())
start-=1
end-=1
k=int(input())
arr = list(map(int, input().split()))
arr = [i-1 for i in arr]
distances1 = dijkstra(start)
distances2 = dijkstra(end)
ans = 987654321123456789
for i in arr:
    ans = min(ans, distances1[i] + distances2[i])
if ans > 98765432112345678:
    print(-1)
else:
    print(ans)