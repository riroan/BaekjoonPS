n=int(input())
arr = list(map(int, input().split()))
arr = [min(2, i) for i in arr]
nodes = [0]*(2*n+1)
nodes[0] = 1
for i in range(1,1+n):
    for j in range(arr[i-1]):
        nodes[i*2-1+j]=1
g = [[]for i in range(10000)]
def f(a,b):
    g[a].append(b)
    g[b].append(a)
if nodes[1]:
    f(0,1)
if nodes[2]:
    f(0,2)
for i in range(3, 2*n+1, 2):
    if nodes[i]:
        f(i, i-2)
    if nodes[i+1]:
        if nodes[i-1]:
            f(i+1, i-1)
        else:
            f(i+1, i-2)
d = [0]*10000
def dfs1(x, p, dd):
    d[x] = dd
    for i in g[x]:
        if i != p:
            dfs1(i, x, dd+1)
dfs1(0, -1, 0)
m= max(d)
ix = 0
for i in range(10000):
    if d[i] == m:
        ix = i
d=  [0]*10000
dfs1(ix, -1, 0)
print(max(d))