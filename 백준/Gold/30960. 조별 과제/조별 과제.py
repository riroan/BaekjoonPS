# author:  riroan
# created:  2023.12.17 13:21:37
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = []
right = []
for i in range(0, n-2, 2):
    left.append(arr[i+1] - arr[i])
for i in range(n-1, 0, -2):
    right.append(arr[i] - arr[i-1])
lp = [0]
rp = [0]
for i in left:
    lp.append(lp[-1]+i)
for i in right:
    rp.append(rp[-1]+i)
rp.reverse()
ans = 10**18
for i in range(len(lp)-1):
    l = lp[i]
    r = rp[i+1]
    m = arr[i*2+2] - arr[i*2]
    ans = min(ans, l+r+m)

print(ans)
