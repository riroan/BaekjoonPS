n = int(input())
arr = [list(map(lambda x:int(x)-1, input().split()))[1:] for i in range(n)]
v = [False] * n
ans = [[], []]


def dfs(x, d=0):
    global v, ans
    v[x] = True
    ans[d].append(x+1)
    for i in arr[x]:
        if not v[i]:
            dfs(i, 1-d)


for i in range(n):
    if not v[i]:
        dfs(i)
if len(ans[1]) == 0:
    ans[1] = [ans[0][-1]]
    ans[0] = ans[0][:-1]
for i in ans:
    print(len(i))
    print(*sorted(i))