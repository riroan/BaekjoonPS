h, n = map(int, input().split())
mod = 10**9+7

dp = [0]*(n+1)
ans = 0
dp[0] = 1
for i in range(1, h+1):
    m = i*(i+1)//2
    if m > n:
        break
    for x in range(n+1-m):
        dp[x+i] += dp[x]
        dp[x+i] %= mod
    ans += dp[n-m]
    ans %= mod
    for x in range(n+1-m):
        dp[x+i]+=dp[x]
        dp[x+i]%=mod
print(ans)
