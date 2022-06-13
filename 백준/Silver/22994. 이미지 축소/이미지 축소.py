from math import gcd
n,m = map(int, input().split())
arr = [list(input()) for i in range(n)]
def f(arr):
    n = len(arr)
    m = len(arr[0])
    ss = set()
    for i in range(n):
        ix = 0
        s = arr[i][0]
        for j in range(m):
            if arr[i][j] !=s:
                ss.add(j-ix)
                ix = j
                s = arr[i][j]
        ss.add(m-ix)
    g = 0
    for i in ss:
        g = gcd(g, i)
    brr = []
    for i in arr:
        t = []
        for j in range(0, len(i), g):
            t.append(i[j])
        brr.append(t)
    return brr

def t(arr):
    r = len(arr)
    c = len(arr[0])
    brr = [[0]*r for i in range(c)]
    for i in range(c):
        for j in range(r):
            brr[i][j] = arr[j][i]
    return brr
arr = t(f(t(f(arr))))

print(len(arr),len(arr[0]))
for i in arr:
    print(''.join(i))

