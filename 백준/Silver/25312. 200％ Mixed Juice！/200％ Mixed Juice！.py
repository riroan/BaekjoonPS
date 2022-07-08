import math
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x: x[0]/x[1])
a, b = 0, 0
c = 0
ix = 0
while m > 0 and ix < n:
    if arr[ix][0] <= m:
        m -= arr[ix][0]
        a += arr[ix][1]
    else:
        b = m*arr[ix][1]
        c = arr[ix][0]
        m = 0
    ix += 1
if c== 0:
    print(f"{a}/1")
else:
    g = math.gcd(a*c+b,c)
    print(f"{(a*c+b)//g}/{c//g}")