def rotate(arr):
    n = len(arr)
    brr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            brr[i][j] = arr[j][n-i-1]
    return brr


def check(x, y, n):
    return 0 <= x < n and 0 <= y < n


def getKey(key):
    n = len(key)
    for i in range(-n+1, n):
        for j in range(-n+1, n):
            brr = [[0]*n for i in range(n)]
            for k in range(n):
                for l in range(n):
                    if check(i+k, j+l, n):
                        brr[k][l]=key[i+k][j+l]
            yield brr

def assign(key, lock):
    n = len(key)
    m = len(lock)
    for i in range(m-n+1):
        for j in range(m-n+1):
            tmp = [t.copy() for t in lock]
            for k in range(n):
                for l in range(n):
                    tmp[i+k][j+l] ^= key[k][l]
            s = 0
            for t in tmp:
                s+=sum(t)
            if s == m**2:
                return True
    return False


def solution(key, lock):
    ok = False
    for i in range(4):
        for k in getKey(key):
            ok|= assign(k, lock)
        key = rotate(key)
    return ok