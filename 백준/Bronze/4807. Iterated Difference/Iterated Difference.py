# author:  riroan
# created:  2023.12.28 09:08:35
import sys
input = lambda: sys.stdin.readline().strip()
ix = 1
while 1:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    ans = 0
    print(f"Case {ix}: ",end="")
    ix += 1
    for ii in range(1000):
        brr = []
        for i in range(n):
            brr.append(abs(arr[(i+1)%n] - arr[i]))
        arr = brr
        if sum(arr) == 0:
            print(ii, "iterations")
            break
    else:
        print("not attained")
