n, h = map(int, input().split())
arr = [int(input()) for i in range(n)]
ans = 10**18
for i in range(2**n):
    t = 0
    for j in range(n):
        if i & (1 << j):
            t += arr[j]
    if t >= h:
        ans = min(ans, abs(t-h))
print(ans)