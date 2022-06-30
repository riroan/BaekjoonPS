from collections import defaultdict
n=int(input())
arr = input().split()
dd = defaultdict(int)
for i in range(n):
    for j in input().split():
        dd[j]+=1
ans = [[i, dd[i]]for i in arr]
ans.sort(key=lambda x:(-x[1], x[0]))
for i in ans:
    print(*i)