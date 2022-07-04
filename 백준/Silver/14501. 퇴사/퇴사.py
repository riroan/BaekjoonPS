n=int(input())
arr = [list(map(int, input().split())) for i in range(n)]
def valid(a):
    if not a:
        return False
    for i in range(len(a)-1):
        if a[i] + arr[a[i]][0] > a[i+1] or a[i]+arr[a[i]][0] > n:
            return False
    
    if a[-1] + arr[a[-1]][0] > n:
        return False
    return True
ans = 0
for i in range(2**n):
    v = []
    for j in range(n):
        if i & (1<<j):
            v.append(j)
    if not valid(v):
        continue
    t = 0
    for i in v:
        t+= arr[i][1]
    ans = max(ans, t)
print(ans)