import sys
input = lambda: sys.stdin.readline().strip()
print("Gnomes:")
for test in range(int(input())):
    a,b,c=map(int, input().split())
    if(b-a)*(c-b)>0:
        print("Ordered")
    else:
        print("Unordered")