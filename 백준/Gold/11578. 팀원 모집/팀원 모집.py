from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split()))[1:] for i in range(m)]
ans = 11
for i in range(1, n+1):
    for j in combinations(arr, i):
        s = []
        for k in j:
            s += k
        if len(set(s)) == n:
            ans=min(ans, i)
print(-1 if ans==11 else ans)