arr = [list(map(int, input().split())) for i in range(9)]
def solve():
    m = 0
    for i in range(9):
        m = max(m,max(arr[i]))
    for i in range(9):
        for j in range(9):
            if arr[i][j] == m:
                print(m)
                print(i+1,j+1)
                return
solve()