# author:  riroan
# created:  2023.10.21 15:02:54
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())+1
arr = [[0, 0, 0, 0]] + [list(map(int, input().split())) for i in range(n-1)]
for i in range(1, n):
    arr[i].extend(list(map(int, input().split())))

g = [[] for i in range(n)]
can = [0]*n
can[0] = 1
for i in range(1, n):
    a,b,c,d = arr[i]
    dist = a+b
    if dist < d:
        can[i] = 1
brr = []
for i in range(n):
    if can[i]:
        brr.append(arr[i])
arr = brr
n = len(arr)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a,b,c,d = arr[i]
        x,y,z,w = arr[j]
        dist = abs(a-x) + abs(b-y)
        if d + dist < w:
            g[i].append((j, w - max(d+dist, z)))
# find longest path in DAG from 0
dp = [0]*n
degree = [0]*n
for i in range(n):
    for x,y in g[i]:
        degree[x] += 1
q = deque([0])
seq = []
while q:
    x = q.popleft()
    seq.append(x)
    for a,b in g[x]:
        degree[a]-=1
        if degree[a] == 0:
            q.append(a)
for i in seq:
    for x,y in g[i]:
        dp[x] = max(dp[x], dp[i] + y)
print(max(dp))

