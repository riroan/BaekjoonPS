n = int(input())
arr = [list(input()) for i in range(n)]
ans = 0
for i in range(n):
    start = -1
    for j in range(n):
        if arr[i][j] == '.' and start == -1:
            start = j
        if arr[i][j] == 'X' and start != -1 and j-start >= 2:
            ans += 1
            # print(i,j)
        if arr[i][j] == 'X':
            start = -1
    if start != -1 and n-start >= 2:
        # print(i)
        ans += 1
aans = 0
for j in range(n):
    start = -1
    for i in range(n):
        if arr[i][j] == '.' and start == -1:
            start = i
        if arr[i][j] == 'X' and start != -1 and i-start >= 2:
            aans += 1
        if arr[i][j] == 'X':
            start = -1
    if start != -1 and n-start >= 2:
        aans += 1
print(ans, aans)
