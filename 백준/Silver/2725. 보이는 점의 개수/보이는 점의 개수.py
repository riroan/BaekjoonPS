import sys
from math import *
input = lambda: sys.stdin.readline().strip()

arr = [[0]*1001 for i in range(1001)]
arr[0][1] = 1
arr[1][0] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        if gcd(i,j) == 1:
            arr[i][j] = 1
dp = [0]*1001
for i in range(1, 1001):
    tmp = i == 1
    for j in range(i):
        tmp+=arr[j][i]+arr[i][j]
    dp[i] = dp[i-1] + tmp

for test in range(int(input())):
    print(dp[int(input())])