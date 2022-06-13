n, m = map(int, input().split())
brr = [[0]*20 for i in range(n+1)]
for _ in range(m):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        b, c = arr[1:]
        brr[b][c-1] = 1
    elif arr[0] == 2:
        b, c = arr[1:]
        brr[b][c-1] = 0
    elif arr[0] == 3:
        b = arr[1]
        for i in range(18,-1,-1):
            brr[b][i+1] = brr[b][i]
        brr[b][0]=0
    elif arr[0] == 4:
        b = arr[1]
        for i in range(1, 20):
            brr[b][i-1] = brr[b][i]
        brr[b][19] = 0

ans = set()
for i in brr[1:]:
    ans.add(tuple(i))
print(len(ans))