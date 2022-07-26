n,m=map(int, input().split())
d = {}
for i in range(n):
    s=input()
    u=int(input())
    d[s] = set()
    for j in range(u):
        d[s].add(input())
for i in range(m):
    s=input()
    op = int(input())
    if op:
        for j in d:
            if s in d[j]:
                print(j)
    else:
        arr = []
        for j in d[s]:
            arr.append(j)
        arr.sort()
        for i in arr:
            print(i)