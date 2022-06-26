r, c, n = map(int, input().split())


def check(x, y):
    return 0 <= x < r and 0 <= y < c


arr = [list(input()) for i in range(r)]
brr = [[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            brr[i][j] = 1
for ii in range(3, n+2):
    if ii % 2:
        for j in range(r):
            for k in range(c):
                if brr[j][k] == 0:
                    brr[j][k] = ii
    else:
        crr = [[brr[i][j]for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if brr[i][j] == ii-3:
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1],[0,0]]:
                        tx, ty = i+dx, j+dy
                        if not check(tx, ty):
                            continue
                        crr[tx][ty] = 0
        brr = crr
    # for i in brr:
    #     print(i)
    # print()
for i in range(r):
    for j in range(c):
        if brr[i][j]:
            print("O", end="")
        else:
            print(".", end="")
    print()
