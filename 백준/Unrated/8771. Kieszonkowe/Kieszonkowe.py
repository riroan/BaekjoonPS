import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    p=1
    s = sum(arr)
    for i in arr:
        p*=i
        if p > s:
            print("ILOCZYN")
            break
    else:
        if p == s:
            print("=")
        else:
            print("SUMA")