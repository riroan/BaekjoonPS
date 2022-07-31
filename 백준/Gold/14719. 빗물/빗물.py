h,w = map(int, input().split())
arr = list(map(int, input().split()))
brr = [[0]*w for i in range(h)]
for i in range(w):
    for j in range(arr[i]):
        brr[j][i] = 1
ans = 0
for i in range(h):
    start = -1
    for j in range(w):
        if brr[i][j] and start == -1:
            start = j
        elif brr[i][j]:
            ans+=j-start-1
            start = j
print(ans)