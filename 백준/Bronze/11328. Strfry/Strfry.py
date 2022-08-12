import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    a,b=input().split()
    a = list(a)
    b=list(b)
    a.sort()
    b.sort()
    if a==b:
        print("Possible")
    else:
        print("Impossible")