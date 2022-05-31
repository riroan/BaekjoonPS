n = int(input())
k = int(input())
g = [[] for i in range(n+1)]

INF = 987654321
arr = [[INF] * n for i in range(n)]
for i in range(n):
    arr[i][i] = 0
for i in range(k):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            arr[i][j] = 0
for i in arr:
    print(*i)