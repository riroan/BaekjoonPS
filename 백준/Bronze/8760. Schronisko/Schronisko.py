import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n,k=map(int, input().split())
    print(n*k//2)