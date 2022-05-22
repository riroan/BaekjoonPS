import heapq
sx, sy = map(float, input().split())
ex, ey = map(float, input().split())


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5


n = int(input())+2
arr = [[sx, sy]] + [list(map(float, input().split()))
                    for i in range(n-2)]+[[ex, ey]]
g = [[987654321]*n for i in range(n)]

for i in range(n):
    for j in range(1, n):
        if i == j:
            # g[i][j] = 0
            continue
        if i == 0:
            g[i][j] = dist(arr[i], arr[j]) / 5
        elif j == n-1:
            g[i][j] = abs(dist(arr[i], arr[j])-50)/5+2
        else:
            g[i][j] = abs(dist(arr[i], arr[j])-50)/5+2


def dijkstra(start):
    distances = [0] * n
    for i in range(n):
        distances[i] = 987654321000
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    v = [[False] * n for i in range(n)]
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if distances[current_destination] < current_distance:
            continue
        for new_destination in range(n):
            if v[current_destination][new_destination]:
                continue
            new_distance = g[current_destination][new_destination]
            if new_destination == current_destination:
                continue
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                v[current_destination][new_destination] = True
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])
    return distances


# print(dijkstra(0)[n-1])


for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])
print(g[0][-1])
