from math import ceil
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n,x=map(int, input().split())
    arr=list(map(int, input().split()))
    brr = [[ceil(i/x), ix] for ix, i in enumerate(arr)]
    brr.sort(key=lambda x:(x[0],x[1]))
    brr = [i[1]+1 for i in brr]
    print(f"Case #{test+1}: ",end="")
    print(*brr)