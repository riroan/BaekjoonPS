n = int(input())
arr = [int(input()) for i in range(n)]
dp = [[[0,0],[0,0]] for i in range(n)]
if n <= 1:
    print(sum(arr))
else:
    dp[0][1] = [arr[0], 1]
    dp[1][0] = [dp[0][1][0] + arr[1], 2]
    dp[1][1] = [arr[1], 1]
    for i in range(2, n):
        if dp[i-1][0][1] != 2:
            dp[i][0] = [arr[i]+dp[i-1][0][0], dp[i-1][0][1]+1]
        if dp[i][0][0] <= dp[i-1][1][0]:
            dp[i][0] = [arr[i]+dp[i-1][1][0], dp[i-1][1][1]+1]
        dp[i][1] = [arr[i]+max(dp[i-2][0][0], dp[i-2][1][0]), 1]
    a = dp[-1][0][0]
    b = dp[-1][1][0]
    print(max(a,b))