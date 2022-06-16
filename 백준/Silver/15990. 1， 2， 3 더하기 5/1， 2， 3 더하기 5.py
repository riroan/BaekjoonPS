import sys
input = lambda: sys.stdin.readline().strip()

dp = [[0,0,0] for i in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]
mod = 10**9+9
for i in range(4, 100001):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] += dp[i-j-1][k]
                dp[i][j] %= mod
for test in range(int(input())):
    n=int(input())
    print(sum(dp[n])%mod)