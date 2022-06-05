board = [[0]*6 for i in range(7)]


def simulation(x, p):
    global board
    ix = 0
    for i in range(5, -1, -1):
        if board[x][i] != 0:
            ix = i+1
            break
    board[x][ix] = p


def check(p):
    for i in range(7):
        for j in range(6):
            for k in range(4):
                if not (0 <= i+k < 7):
                    break
                if board[i+k][j] != p:
                    break
            else:
                return True
            for k in range(4):
                if not (0 <= j+k < 6):
                    break
                if board[i][j+k] != p:
                    break
            else:
                return True
            for k in range(4):
                if not (0 <= j+k < 6) or not(0 <= i+k < 7):
                    break
                if board[i+k][j+k] != p:
                    break
            else:
                return True
            for k in range(4):
                if not (0 <= j-k < 6) or not (0 <= i+k < 7):
                    break
                if board[i+k][j-k] != p:
                    break
            else:
                return True
    return False


for i in range(21):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    simulation(x, 1)
    if check(1):
        print("sk", i+1)
        break
    simulation(y, 2)
    if check(2):
        print("ji", i+1)
        break
else:
    print("ss")