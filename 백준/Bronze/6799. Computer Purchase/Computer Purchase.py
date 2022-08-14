n = int(input())
arr = [input().split() for i in range(n)]
ans = []
for s, x, y, z in arr:
    x = int(x)
    y = int(y)
    z = int(z)
    ans.append((2*x+3*y+z, s))
ans.sort(key=lambda x:(-x[0],x[1]))
for i in range(min(n, 2)):
    print(ans[i][1])