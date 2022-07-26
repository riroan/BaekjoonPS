n, k =map(int, input().split())
arr = [int(input()) for i in range(n)]
dp = [0]*(k+1)

for ix, i in enumerate(arr):
    if i > k:
        continue
    dp[i] += 1
    for j in range(i+1, k+1):
        dp[j] += dp[j-i]
print(dp[-1])