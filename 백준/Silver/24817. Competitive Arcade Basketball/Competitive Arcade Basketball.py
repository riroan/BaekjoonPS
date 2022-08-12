import sys
input = lambda: sys.stdin.readline().strip()
n,m,p=map(int, input().split())
d = {}
for i in range(n):
    d[input()] = 0
ans = []
s=set()
for i in range(p):
    a,b=input().split()
    d[a] += int(b)
    if d[a]>= m and a not in s:
        ans.append(a)
        s.add(a)
if ans:
    for i in ans:
        print(i,"wins!")
else:
    print("No winner!")