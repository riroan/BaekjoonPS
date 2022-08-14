import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr = [input() for i in range(n)]
    brr = [input().split() for i in range(int(input()))]
    d = {}
    for i in arr:
        d[i] = 0
    for i in d:
        for j in brr:
            if i in j:
                d[i] = 1
    print(f"Test set {test+1}:")
    for i in arr:
        if d[i]:
            print(i, "is present")
        else:
            print(i, "is absent")
    print()