n, k =map(int, input().split())
ans = [['.']*k for i in range(n)]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(k):
        r = arr[j*3]
        g = arr[j*3+1]
        b = arr[j*3+2]
        v = 2126*r+7152*g+722*b
        if 0<=v<510000:
            ans[i][j] = '#'
        elif v<1020000:
            ans[i][j] = 'o'
        elif v < 1530000:
            ans[i][j] = '+'
        elif v<2040000:
            ans[i][j] = '-'
    print(''.join(ans[i]))