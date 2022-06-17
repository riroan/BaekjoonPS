n = int(input())
mod = 10**9
dp = [[0]*10 for i in range(n)]
dp[0] = [0]+[1]*9
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][-1] = dp[i-1][-2]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
print(sum(dp[n-1]) % mod)