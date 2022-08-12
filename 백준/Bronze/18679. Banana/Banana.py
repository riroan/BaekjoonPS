import sys
input = lambda: sys.stdin.readline().strip()

d = {}
for test in range(int(input())):
    a,b,c = input().split()
    d[a] = c
for i in range(int(input())):
    input()
    arr = input().split()
    ans = []
    for i in arr:
        ans.append(d[i])
    print(*ans)