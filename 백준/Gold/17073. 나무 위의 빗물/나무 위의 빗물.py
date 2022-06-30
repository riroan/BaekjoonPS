import sys
sys.setrecursionlimit(6*10**5)
input = sys.stdin.readline
n, w = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
cnt = 0
for i in g[2:]:
    if len(i) == 1:
        cnt+=1
print(w/cnt)