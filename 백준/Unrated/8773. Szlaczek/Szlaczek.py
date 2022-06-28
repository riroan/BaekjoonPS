import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n,k = map(int, input().split())
    arr=list(map(int, input().split()))
    arr = arr + arr[::-1]
    print(arr[k%len(arr)])