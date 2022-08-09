n = int(input())
dp = [10**18]*100001
dp[1] = dp[2] = dp[5] = dp[7] = 1
dp[0]=0
for i in range(1, 100001):
    for j in [1,2,5,7]:
        if i-j<0:
            continue
        dp[i] = min(dp[i], dp[i-j] + 1)
print(dp[n])