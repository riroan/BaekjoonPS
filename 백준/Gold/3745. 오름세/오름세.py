import bisect
import sys
input = sys.stdin.readline


def lis(n, arr):
    brr = [-9876543210]
    for i in range(n):
        if arr[i] > brr[-1]:
            brr.append(arr[i])
            continue
        t = bisect.bisect_left(brr, arr[i])
        brr[t] = arr[i]
    return brr

try:
    while True:
        n=int(input())
        arr=list(map(int, input().split()))
        print(len(lis(n,arr))-1)
except:
    pass