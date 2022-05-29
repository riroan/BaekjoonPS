import sys
input = sys.stdin.readline

import bisect

def lis(n, arr):
    brr = [-9876543210]
    for i in range(n):
        if arr[i] > brr[-1]:
            brr.append(arr[i])
            continue
        t = bisect.bisect_left(brr, arr[i])
        brr[t] = arr[i]
    return brr


for test in range(int(input())):
    n,k=map(int, input().split())
    arr=list(map(int, input().split()))
    print(f"Case #{test+1}")
    print(int(len(lis(n, arr)) - 1 >= k))