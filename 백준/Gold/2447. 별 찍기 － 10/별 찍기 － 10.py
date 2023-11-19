# author:  riroan
# created:  2023.11.18 18:10:48
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())


def go(brr, n):
    crr = [[' '] * len(brr) for i in range(len(brr))]
    v = [[1, 1, 1],  [1, 0, 1], [
        1, 1, 1]]
    arr = [[' ' for i in range(3*len(brr))] for j in range(len(brr) * 3)]

    for i in range(3):
        for j in range(3):
            if v[i][j]:
                cur = brr
            else:
                cur = crr
            for k in range(len(cur)):
                for l in range(len(cur)):
                    arr[i * len(brr)+k][j * len(brr)+l] = cur[k][l]
    if n > 3:
        go(arr, n // 3)
    else:
        for i in arr:
            print(''.join(i))

go([['*']], n)
