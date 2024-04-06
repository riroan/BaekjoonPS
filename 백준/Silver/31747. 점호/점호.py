# author:  riroan
# created:  2024.04.06 13:23:09
import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())
arr = list(map(int, input().split()))
a = deque()
b = deque()
for i in range(n):
    if arr[i] == 1:
        a.append(i)
    else:
        b.append(i)
ans = 0
t = 0
while a and b:
    if a[0] < t + k and b[0] < t+k:
        t += 2
        a.popleft()
        b.popleft()
    elif a[0] < t+k:
        t += 1
        a.popleft()
    else:
        t += 1
        b.popleft()
    ans += 1
print(ans+len(a) + len(b))
