from collections import defaultdict
n,c = map(int, input().split())
arr = list(map(int, input().split()))
d = defaultdict(int)
for i in arr:
    d[i]+=1
cnt = []
for i in d:
    cnt.append((i, d[i]))
cnt.sort(key=lambda x:-x[1])
for i, j in cnt:
    for k in range(j):
        print(i, end=" ")