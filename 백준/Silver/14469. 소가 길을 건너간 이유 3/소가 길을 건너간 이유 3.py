n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key = lambda x: (x[0], x[1]))
ans = 0
for x, y in arr:
    ans = max(ans, x)+y
print(ans)