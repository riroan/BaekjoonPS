import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    arr = input().split()
    brr = input().split()
    crr = input().split()
    d = {}
    dd = {}
    for i in range(n):
        d[brr[i]] = arr[i]
        dd[brr[i]] = crr[i]
    for i,j in zip(arr, brr):
        print(dd[d[j]], end=" ")
    print()