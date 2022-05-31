import sys
from collections import defaultdict
input = sys.stdin.readline

for test in range(int(input())):
    n=int(input())
    arr = [input().strip().split() for i in range(n)]
    d = defaultdict(int)
    for i, j in arr:
        d[j]+=1
    ans = 1
    for i in d:
        ans*=d[i]+1
    print(ans-1)