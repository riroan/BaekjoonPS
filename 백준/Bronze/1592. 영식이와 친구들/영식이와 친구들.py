# author:  riroan
# created:  2023.11.25 10:07:54
import sys
input = lambda: sys.stdin.readline().strip()


n,m,l = map(int, input().split())
arr = [0]*n
cur = 0
ans = 0
while 1:
    arr[cur] += 1
    if arr[cur] == m:
        break

    if arr[cur] % 2:
        cur = (cur + l) % n
    else:
        cur = (cur - l) % n
    ans+=1
print(ans)
