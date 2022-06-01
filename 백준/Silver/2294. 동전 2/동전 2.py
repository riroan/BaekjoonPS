inf = 123456789987654321
dp = [inf]*100001
n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
for i in arr:
    dp[i] = 1
for i in range(1, k+1):
    if dp[i] == inf:
        for j in range(i//2+1):
            dp[i] = min(dp[i], dp[j] + dp[i-j])
if dp[k] == inf:
    print(-1)
else:
    print(dp[k])