from collections import defaultdict
n=int(input())
arr = [list(map(int, input().split())) for i in range(n)]
brr = [[0]*n for i in range(3)]
for i in range(n):
    for j in range(3):
        brr[j][i] = arr[i][j]
ans = [0]*n
for i in range(3):
    d = defaultdict(int)
    for j in range(n):
        d[brr[i][j]]+=1
    for j in range(n):
        if d[brr[i][j]] ==1:
            ans[j]+=brr[i][j]
for i in ans:
    print(i)