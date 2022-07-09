import sys
sys.setrecursionlimit(10**5)
def input(): return sys.stdin.readline().strip()

def dfs(x, flag = 0):
    global ok
    v[x] = 1
    if flag:
        a.add(x)
    else:
        b.add(x)
    for i in g[x]:
        if (i in a and x in a) or (i in b and x in b):
            ok = False
        if not v[i]:
            dfs(i, 1-flag)

for test in range(int(input())):
    n, k = map(int, input().split())
    g = [[]*n for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    v = [0]*n
    ok = True
    a, b = set(), set()
    for i in range(n):
        if not v[i]:
            dfs(i)
    if ok:
        print("YES")
    else:
        print("NO")