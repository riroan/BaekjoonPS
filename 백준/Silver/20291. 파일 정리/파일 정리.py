from collections import defaultdict
n=int(input())
arr = [input().split(".") for i in range(n)]
d = defaultdict(int)
for x,y in arr:
    d[y]+=1
v = []
for i in d:
    v.append((i, d[i]))
v.sort(key=lambda x:x[0])
for i in v:
    print(*i)