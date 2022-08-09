import sys
input = lambda: sys.stdin.readline().strip()
dp = [1]*1001
dp[0] = 0
for i in range(1, 1001):
    for j in range(i+1):
        if (i-j)%2==0:
            dp[i] = dp[i] + dp[(i-j)//2]
for test in range(int(input())):
    n=int(input())
    ans = 0
    for i in range(n+1):
        if (n-i)%2 == 0:
            ans+=dp[(n-i)//2]
    print(ans+1)