from math import gcd
n, s = map(int, input().split())
arr = list(map(int, input().split()))
m = min([s]+arr)
s-=m
arr = [i-m for i in arr]
ans = s
for i in arr:
    ans = gcd(ans, i)
print(ans)