import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
s = set()
for i in arr:
    s.add(tuple(i))
mi, ma = {}, {}
for l, r in arr:
    if  l not in ma:
        ma[l] = r
    else:
        ma[l] = max(ma[l], r)
    if r not in mi:
        mi[r] = l
    else:
        mi[r] = min(mi[r], l)

for _ in range(int (input())):
    a,b=map(int, input().split())
    if (a,b) in s:
        print(1)
        continue
    x,y = -1,-1
    if a in ma:
        x = ma[a]
    if b in mi:
        y = mi[b]
    if x == -1 or y == -1:
        print(-1)
        continue
    if y<=a and b<=x:
        print(2)
    else:
        print(-1)