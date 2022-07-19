from math import *
import sys
input = lambda: sys.stdin.readline().strip()

n=int(input())
arr = [int(input()) for i in range(n)]
arr.sort() # nlogn
tmp = []
for i in range(n-1): # n
    tmp.append(arr[i+1]-arr[i])
step = tmp[0]
for i in tmp[1:]: # n log(max A)
    step = gcd(step, i)
start = arr[0]
end = arr[-1]
cnt = (end-start)//step+1
print(cnt-n)