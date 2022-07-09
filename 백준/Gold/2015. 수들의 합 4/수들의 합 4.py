from collections import defaultdict
n,k = map(int, input().split())
d = defaultdict(int)
ans = 0
arr = list(map(int, input().split()))
ps = [0]
d[0] += 1
for i in arr:
    ps.append(i+ps[-1])
    if ps[-1] - k in d:
        ans += d[ps[-1] - k]
    d[ps[-1]] += 1
print(ans)