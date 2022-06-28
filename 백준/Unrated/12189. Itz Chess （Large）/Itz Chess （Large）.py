import sys
def input(): return sys.stdin.readline().strip()


def check(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def vertical(x,y):
    global ans
    for i in range(1, 8):
        tx,ty = x+i,y
        if check(tx,ty):
            if board[tx][ty] !=' ':
                ans+=1
                break
    for i in range(1, 8):
        tx, ty = x-i, y
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break


def horizontal(x, y):
    global ans
    for i in range(1, 8):
        tx, ty = x, y+i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break
    for i in range(1, 8):
        tx, ty = x, y-i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break

def rightup(x,y):
    global ans
    for i in range(1, 8):
        tx, ty = x-i, y+i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break
    for i in range(1, 8):
        tx, ty = x+i, y-i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break


def leftup(x, y):
    global ans
    for i in range(1, 8):
        tx, ty = x+i, y+i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break
    for i in range(1, 8):
        tx, ty = x-i, y-i
        if check(tx, ty):
            if board[tx][ty] != ' ':
                ans += 1
                break


for test in range(int(input())):
    # if test:
    #     input()
    n = int(input())
    arr = [input().split('-') for i in range(n)]
    board = [[' '] * 8 for i in range(8)]
    for x, y in arr:
        a, b = x[0], x[1]
        a = ord(a) - ord('A')
        b = int(b)-1
        board[a][b] = y
    ans = 0
    for x in range(8):
        for y in range(8):
            b = board[x][y]
            if b == 'K':
                for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]:
                    tx, ty = x+dx, y+dy
                    if check(tx, ty):
                        if board[tx][ty] != ' ':
                            ans += 1
            elif b == 'Q':
                horizontal(x,y)
                vertical(x,y)
                leftup(x,y)
                rightup(x,y)
            elif b == 'R':
                horizontal(x, y)
                vertical(x, y)
            elif b == 'B':
                leftup(x, y)
                rightup(x, y)
            elif b == 'N':
                for dx, dy in [[-2, 1], [1, -2], [2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [-1, -2]]:
                    tx, ty = x+dx, y+dy
                    if check(tx, ty):
                        if board[tx][ty] != ' ':
                            ans += 1
            elif b == 'P':
                for dx, dy in [[1,1], [1,-1]]:
                    tx,ty = x+dx, y+dy
                    if check(tx,ty):
                        if board[tx][ty] != ' ':
                            ans += 1
    print(f"Case #{test+1}: ",end="")
    print(ans)
