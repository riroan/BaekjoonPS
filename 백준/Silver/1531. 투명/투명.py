n,m = map(int, input().split())
arr = [[0] * 100 for i in range(100)]
for i in range(n):
    x1,y1,x2,y2=map(int, input().split())
    for x in range(x1-1, x2):
        for y in range(y1-1,y2):
            arr[x][y]+=1
ans = 0
for i in arr:
    for j in i:
        if j > m:
            ans+=1
print(ans)