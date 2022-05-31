n = int(input())
k = int(input())
arr = []
if k:
    arr = set(list(map(int, input().split())))
arr = [i for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] if i not in arr]
ans = abs(n-100)

def dfs(x='', d=1):
    global ans
    if len(x) == 7:
        return
    for i in arr:
        y = x+str(i)
        ans = min(ans, d + abs(n-int(y)))
        dfs(y, d+1)
dfs()

print(ans)