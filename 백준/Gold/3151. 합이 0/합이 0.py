from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().strip()

n=int(input())
arr = list(map(int, input().split()))
d = defaultdict(int)
if n <= 2:
    print(0)
else:
    d[arr[0]+arr[1]] = 1
    ans = 0
    for i in range(2, n):
        ans+=d[-arr[i]]
        for j in range(i):
            d[arr[j]+arr[i]] += 1
    
    print(ans)