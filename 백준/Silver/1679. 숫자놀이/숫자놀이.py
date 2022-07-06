n = int(input())
arr = list(map(int, input().split()))
k = int(input())
dp = [10**18]*2000000
dp[0] = 0
for x in range(2000000):
    for i in arr:
        if x+i < 2000000:
            dp[x+i] = min(dp[x+i], dp[x]+1)
for i in range(1, 2000000):
    if dp[i]>k:
        ix = i
        break
if ix & 1:
    print(f"jjaksoon win at {ix}")
else:
    print(f"holsoon win at {ix}")
