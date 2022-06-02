n,m = map(int, input().split())
arr = list(map(int, input().split()))
ps = [0]
for i in arr:
    ps.append(ps[-1]+i)
ans = -10**10
for i in range(len(ps)-m):
    ans = max(ans, ps[i+m]-ps[i])
print(ans)