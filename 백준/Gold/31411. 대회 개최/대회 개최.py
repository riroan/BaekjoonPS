# author:  riroan
# created:  2024.02.18 11:12:17
import sys
def input(): return sys.stdin.readline().strip()


def add(i):
    global s
    _, x = arr[i]
    brr[x] += 1
    if brr[x] == 1:
        s += 1


def sub(i):
    global s
    _, x = arr[i]
    brr[x] -= 1
    if brr[x] == 0:
        s -= 1


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.extend([[j, i] for j in list(map(int, input().split()))])
arr.sort()
s = 0
brr = [0]*n
l = 0
r = 0
ans = 10**18
while r < len(arr):
    add(r)
    while s == n:
        ans = min(ans, arr[r][0] - arr[l][0])
        sub(l)
        l += 1
    r += 1
print(ans)
