n = int(input())
arr = input().split()
arr = [int(i) for i in arr]
dp = [0] * n
dp[0] = 1
for i in range(1,n):
    m = 0
    for j in range(i-1,-1,-1):
        if arr[i] > arr[j]:
            if m < dp[j]:
                m = dp[j]

    dp[i] = m+1
print(max(dp))