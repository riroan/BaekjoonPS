from bisect import *
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(m):
    a,b=map(int, input().split())
    l = bisect_left(arr, a)
    r = bisect_right(arr, b)
    print(r-l)
