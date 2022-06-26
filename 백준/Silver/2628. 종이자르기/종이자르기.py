n,m = map(int, input().split())
arr = [list(map(int, input().split())) for i  in range(int(input()))]
row = []
col = []
for x,y in arr:
    if x == 0:
        row.append(y)
    else:
        col.append(y)
row += [0, m]
col += [0, n]
row.sort()
col.sort()
ans = 0
for i in range(1, len(row)):
    for j in range(1, len(col)):
        ans = max(ans, (row[i]-row[i-1])*(col[j]-col[j-1]))
print(ans)