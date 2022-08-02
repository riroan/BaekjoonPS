def lis(n, arr):
    dp = [0] * n
    dp[0] = 1
    for i in range(1,n):
        m = 0
        for j in range(i-1,-1,-1):
            if arr[i] > arr[j]:
                if m < dp[j]:
                    m = dp[j]

        dp[i] = m+1
    return dp


n = int(input())
arr = list(map(int, input().split()))
a = lis(n, arr)
b = lis(n, arr[::-1])
ans = 0
for i,j in zip(a,b[::-1]):
    ans = max(ans, i+j-1)
print(ans)