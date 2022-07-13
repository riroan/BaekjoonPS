import sys
input = lambda: sys.stdin.readline().strip()

def dfs(x):
    global ans
    ans+=1
    for i in g[x]:
        if not v[i]:
            dfs(i)

for test in range(int(input())):
    n=int(input())
    arr = list(map(int, input().split()))
    print(f"Case #{test+1}:")
    g = [[] for i in range(n)]
    for i in range(n):
        g[arr[i]-1].append(i)
    for i in range(n):
        v = [0]*n
        v[i] = 1
        ans = 0
        dfs(i)
        print(ans)