n=int(input())
arr = [list(input()) for i in range(n)]
brr = [[0]*n for i in range(n)]
def check(x,y):
    return 0<=x<n and 0<=y<n
for i in range(n):
    for j in range(n):
        try:
            int(arr[i][j])
            brr[i][j] = '*'
            continue
        except:
            pass
        tmp = 0
        for dx, dy in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            tx,ty = i+dx,j+dy
            if not check(tx,ty):
                continue
            try:
                tmp += int(arr[tx][ty])
            except:
                pass
        if tmp >= 10:
            tmp = 'M'
        brr[i][j] = str(tmp)
for i in brr:
    print(''.join(i))
