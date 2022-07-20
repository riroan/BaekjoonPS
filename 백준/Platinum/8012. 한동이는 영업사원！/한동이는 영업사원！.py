import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(40000)
n = int(input())
g = [[] for i in range(n+5)]
par = [0] * (n+5)
sz = [0] * (n+5)
dist = [0]*(n+5)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append((b, 1))
    g[b].append((a, 1))


def dfs(x, p, d = 0):
    global sz
    par[x] = p
    sz[x] = 1
    dist[x] = d
    for i, j in g[x]:
        if i != p:
            sz[x] += dfs(i, x, d+j)
    return sz[x]


depth = [0]*(n+5)
chain_number = [0]*(n+5)
chain_index = [0]*(n+5)
chain = [[] for i in range(n+5)]



def HLD(i, p, cur_chain, d):
    depth[i] = d
    chain_number[i] = cur_chain
    chain_index[i] = len(chain[cur_chain])
    chain[cur_chain].append(i)

    heavy = -1
    for x,_ in g[i]:
        if x != p and (heavy == -1 or heavy != -1 and sz[x] > sz[heavy]):
            heavy = x
    if heavy != -1:
        HLD(heavy, i, cur_chain, d)
    for x,_ in g[i]:
        if x != p and x != heavy:
            HLD(x, i, x, d+1)


dfs(1, 0)
HLD(1, 0, 1, 0)


def LCA(a, b):
    while chain_number[a] != chain_number[b]:
        if depth[a] > depth[b]:
            a = par[chain_number[a]]
        else:
            b = par[chain_number[b]]
    if chain_index[a] > chain_index[b]:
        return b
    else:
        return a


m=int(input())
arr = [int(input()) for i in range(m)]
ans = 0
for i in range(m-1):
    a,b = arr[i], arr[i+1]
    c = LCA(a,b)
    tmp = dist[a]+dist[b] - 2*dist[c]
    ans+=tmp
print(ans)